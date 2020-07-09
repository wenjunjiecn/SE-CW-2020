<template>
  <div class="app-container">

    <div>
      <FilenameOption v-model="filename" />
      <!-- <AutoWidthOption v-model="autoWidth" /> -->
      <BookTypeOption v-model="bookType" />
      <el-button :loading="downloadLoading" style="margin:0 0 20px 20px;" type="primary" icon="el-icon-document" @click="handleDownload">
        导出Excel
      </el-button>
      <el-button  style="margin:0 0 20px 20px;" type="primary" icon="el-icon-info" @click="handleUrge">
        一键催收超期
      </el-button>

    </div>

    <el-table v-loading="listLoading" :data="list" element-loading-text="加载中,请稍后" border fit highlight-current-row>
      <el-table-column align="center" label="序号" width="95">
        <template slot-scope="scope">
          {{ scope.$index }}
        </template>
      </el-table-column>
      <el-table-column label="书名">
        <template slot-scope="scope">
          {{ scope.row.bookName }}
        </template>
      </el-table-column>
      <el-table-column label="ISDN" width="160" align="center">
        <template slot-scope="scope">
          <el-tag>{{ scope.row.ISDN }}</el-tag>
        </template>
      </el-table-column>
      <el-table-column label="用户ID" width="115" align="center">
        <template slot-scope="scope">
          {{ scope.row.readID }}
        </template>
      </el-table-column>
      <el-table-column label="用户姓名" width="115" align="center">
        <template slot-scope="scope">
          {{ scope.row.username }}
        </template>
      </el-table-column>
      <el-table-column label="专业" width="115" align="center">
        <template slot-scope="scope">
          {{ scope.row.major }}
        </template>
      </el-table-column>

      <el-table-column align="center" label="借阅时间" width="220">
        <template slot-scope="scope">
          <i class="el-icon-time" />
          <span>{{ scope.row.time | parseTime('{y}-{m}-{d} {h}:{i}') }}</span>
        </template>
      </el-table-column>
      <el-table-column label="剩余天数" width="115" align="center" sortable='true'>
        <template slot-scope="scope" >
          {{ scope.row.leftday }}
        </template>
      </el-table-column>

    </el-table>
  </div>
</template>

<script>
import { fetchList } from '@/api/article'
import { parseTime } from '@/utils'
// options components
import FilenameOption from './components/FilenameOption'
import AutoWidthOption from './components/AutoWidthOption'
import BookTypeOption from './components/BookTypeOption'
import axios from 'axios';
import gettoken from '../../../src/store/modules/user.js'
export default {
  name: 'ExportExcel',
  components: { FilenameOption, AutoWidthOption, BookTypeOption },
  data() {
    return {
      list: null,
      listLoading: true,
      downloadLoading: false,
      filename: '借阅信息表',
      autoWidth: true,
      bookType: 'xlsx',

    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      this.listLoading = true
      var vm=this
      this.loading=true;
      const path = 'http://127.0.0.1:5000/api/getBorrowList';
            axios.get(path,{params:{token:gettoken.state.token}
               
              })
              .then((res) => {
                this.list = res.data;
                this.listLoading = false
              })
              .catch((error) => {
                // eslint-disable-next-line
                vm.$message({
                        type: 'info',
                        message: '出错啦！获取数据失败'
                });
                this.loading=false
              });
    },
    handleDownload() {
      this.downloadLoading = true
      import('@/vendor/Export2Excel').then(excel => {
        const tHeader = [ '书名', 'ISDN', '用户ID', '用户姓名','专业','借阅时间','剩余天数']
        const filterVal = [ 'bookName', 'ISDN', 'readID', 'username','major','time','leftday']
        const list = this.list
        const data = this.formatJson(filterVal, list)
        excel.export_json_to_excel({
          header: tHeader,
          data,
          filename: this.filename,
          autoWidth: this.autoWidth,
          bookType: this.bookType
        })
        this.downloadLoading = false
      })
    },
    formatJson(filterVal, jsonData) {
      return jsonData.map(v => filterVal.map(j => {
        if (j === 'timestamp') {
          return parseTime(v[j])
        } else {
          return v[j]
        }
      }))
    },
    handleUrge(row) {
      var vm=this
        this.$confirm('确认给所有超期用户发送催收通知吗', '提示', {
                  confirmButtonText: '确定',
                  cancelButtonText: '取消',
                  type: 'warning'
                }).then(() => {
                  axios.post('http://127.0.0.1:5000/api/urge', {
                    
                     token:gettoken.state.token

                    })

                    .then(function (response) {
                    //  this.$refs[temp].resetFields();
                      vm.$message({
                          type: 'success',
                          message: '操作成功!'
                        });
                    })
                    .catch(function (error) {
                      vm.$message({
                          type: 'info',
                          message: error
                        });
                  })

                  setTimeout(() => {
                    this.fetchData()
                  }, 1.5 * 1000)
                }).catch(() => {
                  this.$message({
                    type: 'info',
                    message: '已取消操作'
                  });
                });
    },
  }
}
</script>

<style>
.radio-label {
  font-size: 14px;
  color: #606266;
  line-height: 40px;
  padding: 0 12px 0 30px;
}
</style>
