<template>
  <div class="block">
    <el-table :data="timeline" style="width: 100%" sort='time' :default-sort="{prop: 'time', order: 'descending'}">
      <el-table-column label="标题" width="300">
        <template slot-scope="scope">
          <a class="buttonText listtitle" @click="detail(scope.row)"> {{ scope.row.title }}</a>

        </template>
      </el-table-column>
      <el-table-column label="摘要" width="300">
        <template slot-scope="scope">
          <a class="buttonText listtitle" @click="detail(scope.row)"> {{ scope.row.content_short }}</a>
        </template>
      </el-table-column>
      <el-table-column prop="author" label="作者" width="100">
      </el-table-column>
      <el-table-column prop="time" label="发布时间">
      </el-table-column>
      <el-table-column label="操作" width="180" >
        <template slot-scope="scope">
          <el-tag @click="detail(scope.row)"   size="small" v-permission="['user']">查看</el-tag>
          <el-tag @click="handleDelete(scope.row)" type="danger" size="small" v-permission="['admin']">删除</el-tag>
        </template>
      </el-table-column>
    </el-table>

    </el-card>

    <el-dialog :visible.sync="dialogVisible" width="100%" fullscreen='true' modal='false' >

      <div width='60%' align="center" style="margin: 0 200px;">

        <h1 style="text-align: left;  font: black; font-size: 34px;margin-top: 12px;margin-bottom: 10px;">{{detailList.title}}</h1>
        <p style="text-align: left; font-weight:bold">作者:{{detailList.author}}</p>
        <p style="text-align: left;  line-height: 2.2;margin-bottom: 2em;overflow-wrap: break-word;word-wrap: break-word;">摘要:{{detailList.content_short}}</p>
        <p class="dialog_content" style="text-align: left;font-size: 16px Microsoft Yahei,Avenir,Segoe UI,Hiragino Sans GB,STHeiti,Microsoft Sans Serif,WenQuanYi Micro Hei,sans-serif;  line-height: 2.2;margin-bottom: 2em;overflow-wrap: break-word;word-wrap: break-word;"
          v-html="detailList.content"></p>

      </div>



    </el-dialog>
  </div>
</template>

<script>
  import axios from 'axios';
  import gettoken from '../../../../src/store/modules/user.js'
  import permission from '@/directive/permission/index.js'
  export default {
    directives: { permission },
    data() {
      return {
        dialogVisible: false,
        initSuccess: false,
        timeline: [],
        tag: true,
        totalCount: 1,
        detailList: {
          title: '初始化',
          author: '',
          content_short: '',
          content: '',
          time: '',
          important: '',

        },

      }
    },
    created() {

      this.getList()
    },
    methods: {
      getList() {
        var vm = this
        let mytoken = gettoken.state.token
        const path = 'http://127.0.0.1:5000/api/announcement';
        axios.get(path, {
            params: {
              token: mytoken
            }
          })
          .then((res) => {
            vm.timeline = res.data;
            // vm.totalCount=Object.keys(this.list).length;
            vm.initSuccess = true
            vm.$message({
              message: '数据加载完成',
              type: 'success'
            });
          })
          .catch((error) => {

            vm.$message({
              type: 'info',
              message: '获取数据失败，请检查网络' + error
            });

          });


      },
      handleDelete(row) {
        var vm = this
        this.$confirm('您即将删除一条公告，确定吗', '提示', {
          confirmButtonText: '确定删除',
          cancelButtonText: '点错了',
          type: 'warning'
        }).then(() => {
          axios.post('http://127.0.0.1:5000/api/deleteann', {
              annID: row.mesID
            })

            .then(function(response) {
              //  this.$refs[temp].resetFields();
              vm.$message({
                type: 'success',
                message: '删除成功!'
              });
            })
            .catch(function(error) {
              vm.$message({
                type: 'info',
                message: error
              });
            })

          setTimeout(() => {
            this.getList()
          }, 1.5 * 1000)
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          });
        });
      },

      detail(item) {
        this.detailList.title = item.title;
        this.detailList.author = item.author;
        this.detailList.content_short = item.content_short;
        this.detailList.content = item.content;
        this.detailList.time = item.time;
        this.detailList.important = item.important;

        this.dialogVisible = true
      },
      tableRowClassName({
        row,
        rowIndex
      }) {
        if (row.important == 1) {
          return 'important_1';
        } else if (row.important == 2) {
          return 'important_2';
        } else if (row.important == 3) {
          return 'important_3';
        }
        return '';
      }
    }
  }
</script>

<style>
  .listtitle {
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 3;
    overflow: hidden;
  }

  .listtitle:hover {
    color: #1890FF;
  }

  .text {
    font-size: 14px;
  }

  .item {
    padding: 5px 0;
  }

  .box-card {
    margin: 0 auto;
    width: 90%;
    margin-bottom: 20px;
  }

  .el-table .important_1 {
    background: #99A9BF;
  }

  .el-table .important_2 {
    background: #F7BA2A;
  }

  .el-table .important_3 {
    background: #FF9900;
  }

  .dialog_content img {

    width: 100%;

  }
</style>
