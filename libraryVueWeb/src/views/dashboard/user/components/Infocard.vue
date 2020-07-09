<template>
  <el-card style="margin-bottom:20px;">
    <div slot="header" class="clearfix">
      <span>消息</span>
    </div>
    <el-table
          :data="datalist"
          :show-header='false'
          style="width: 100%">
          <el-table-column
          width="30"
            >
            <template  slot-scope="scope">
             <a @click="handleDelete(scope.row)"> <i class="el-icon-error" /> </a>
            </template>
          </el-table-column>
          <el-table-column
            width='120'>
            <template slot-scope="scope">
              <el-tag  @click="detail(scope.row)"> {{ scope.row.author }}</el-tag>
            </template>
          </el-table-column>
          <el-table-column
            >
            <template slot-scope="scope">
              <a  @click="detail(scope.row)"> {{ scope.row.title }},点击查看详情</a>
            </template>
          </el-table-column>


     </el-table>

    </div>

    <el-dialog
      title='详情'
      :visible.sync="dialogFormVisible"
      width="30%"
      center="true"
      >
     <!-- <span>{{detailList.content}}</span> -->
      <p class="dialog_content"
        v-html="detailList.content"></p>
    </el-dialog>




  </el-card>






</template>

<script>
import PanThumb from '@/components/PanThumb'
import axios from 'axios';
import gettoken from '../../../../../src/store/modules/user.js'
export default {

  data(){
    return{
      dialogFormVisible:false,
      datalist:'',
      detailList:{
        title:'',
        content:'',
     },
    }
  },
  created() {
    this.getList()

  },
  methods:{
    getList(){
      var vm=this
      let mytoken=gettoken.state.token
      const path = 'http://127.0.0.1:5000/api/getinfolist';
            axios.get(path,{params:{token:mytoken}})
              .then((res) => {
                vm.datalist = res.data;
                vm.$message({
                          message: '数据加载完成',
                          type: 'success'
                 });
              })
              .catch((error) => {

                vm.$message({
                        type: 'info',
                        message: '获取数据失败，请检查网络'+error
                });

              });


    },
    detail(row){
            this.dialogFormVisible=true;
            this.detailList.title=row.author;
            this.detailList.content=row.content

    },
    handleDelete(row){
            var vm = this
            this.$confirm('您即将删除一条消息，确定吗', '提示', {
              confirmButtonText: '确定删除',
              cancelButtonText: '点错了',
              type: 'warning'
            }).then(() => {
              axios.post('http://127.0.0.1:5000/api/deleteinfo', {
                  token:gettoken.state.token,
                  infoid: row.infoid
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


  },

}
</script>

<style lang="scss" scoped>
 .box-center {
   margin: 0 auto;
   display: table;
 }

 .text-muted {
   color: #777;
 }






</style>
