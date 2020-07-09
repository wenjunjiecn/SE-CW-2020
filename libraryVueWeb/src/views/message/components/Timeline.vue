<template>
  <div class="block">
    <el-table :data="timeline" style="width: 100%" :default-sort="{prop: 'addtime', order: 'descending'}">
      <el-table-column label="留言内容" width="300">
        <template slot-scope="scope">
          <a class="buttonText listtitle" @click="detail(scope.row)"> {{ scope.row.content }}</a>
        </template>
      </el-table-column>
      <el-table-column label="用户ID" width="300">
        <template slot-scope="scope">
          <p> {{ scope.row.readID }}</p>
        </template>
      </el-table-column>
      <el-table-column prop="addtime" label="留言时间">

      </el-table-column>
      <el-table-column label="操作" width="180">
        <template slot-scope="scope">
          <p type="text" size="small" v-permission="['user']">无操作权限</p>
          <el-tag @click="handleReMes(scope.row)"   v-permission="['admin']">回复</el-tag>
          <el-tag @click="handleDelete(scope.row)" type="danger"  v-permission="['admin']">删除</el-tag>
        </template>
      </el-table-column>
    </el-table>

    </el-card>

    <el-dialog :visible.sync="dialogVisible" width="100%" fullscreen='true' modal='false'>

      <div width='60%' align="center" style="margin: 0 200px;">

        <h1 style="text-align: left;  font: black; font-size: 34px;margin-top: 12px;margin-bottom: 10px;">留言详情</h1>
        <p style="text-align: left; font-weight:bold">读者学号:{{detailList.readID}}</p>
        <p style="text-align: left;  line-height: 2.2;margin-bottom: 2em;overflow-wrap: break-word;word-wrap: break-word;">{{detailList.content_short}}</p>

        <p class="dialog_content" style="text-align: left;font-size: 16px Microsoft Yahei,Avenir,Segoe UI,Hiragino Sans GB,STHeiti,Microsoft Sans Serif,WenQuanYi Micro Hei,sans-serif;  line-height: 2.2;margin-bottom: 2em;overflow-wrap: break-word;word-wrap: break-word;"
          v-html="detailList.content"></p>

      </div>


    </el-dialog>

    <el-dialog title="回复留言" :visible.sync="showmessagetext" width="180"  modal='false'>

      <div width='100%' align="center" style="margin: 10px;">
        <el-input
          type="textarea"
          :rows="10"
          placeholder="请输入留言内容"
          :max="200"
          v-model="postForm.content">
        </el-input>



      </div>
      <div slot="footer" class="dialog-footer">
          <el-button type="primary" @click="submitForm">发送</el-button>
       </div>


    </el-dialog>




  </div>
</template>

<script>
  import Sticky from '@/components/Sticky'
  import Tinymce from '@/components/Tinymce'
  import axios from 'axios';
  import permission from '@/directive/permission/index.js' // 权限判断指令
  import gettoken from '../../../../src/store/modules/user.js'
  export default {
    directives: {
      permission
    },
    components: {
      Tinymce,
      Sticky
    },
    data() {
      return {
        dialogVisible: false,
        initSuccess: false,
        showmessagetext:false,
        timeline: [],
        tag: true,
        msg: '',
        totalCount: 1,
        detailList: {

          content: '',
          mesID: '',
          readID: '',
          addtime: '',


        },
        postForm: {
          content: '', // 文章内容
        },
        rules: {

          content: [{
              required: true,
              message: '请输入发布内容',
              trigger: 'blur'
            },
            {
              min: 2,
              max: 2000,
              message: '生成的html长度在 2 到 2000 个字符',
              trigger: 'blur'
            }
          ],

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
        const path = 'http://127.0.0.1:5000/api/message';
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
        this.$confirm('您即将删除一条留言，确定吗', '提示', {
          confirmButtonText: '确定删除',
          cancelButtonText: '点错了',
          type: 'warning'
        }).then(() => {
          axios.post('http://127.0.0.1:5000/api/deletemessage', {

              mesID: row.mesID
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
        this.detailList.addtime = item.addtime;
        this.detailList.content = item.content;
        this.detailList.mesID = item.mesID;
        this.detailList.readID = item.readID;


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
      },
      submitForm() {
        var vm = this
        console.log(this.postForm)
        const path = 'http://127.0.0.1:5000/api/remessage';
        axios.post(path, {
            content: '<h3>回复消息</h3>'+vm.postForm.content + '<hr /> <h4>消息原文</h4>'+ vm.detailList.content,
            readid: vm.detailList.readID,
            token: gettoken.state.token
          })

          .then(function(response) {
            //  this.$refs[temp].resetFields();
              vm.$message({
                message: '发送成功',
                type: 'success'
              });
              vm.detailList.content='';
              vm.showmessagetext=false;

          })
          .catch(function(error) {
            vm.$message({
              type: 'info',
              message: '发布失败'
            });

          })
        this.loading = false
      },
      handleReMes(row){
        this.detailList.content=row.content;
        this.detailList.mesID=row.mesID;
        this.detailList.readID= row.readID;
        this.detailList.addtime= row.addtime;
        this.showmessagetext=true;
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
