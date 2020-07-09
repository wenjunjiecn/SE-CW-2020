<template>
  <div class="app-container">
    <div class="filter-container">
      <el-tooltip content="选择检索类型" effect="dark" placement="bottom">
        <el-select class="filter-item" v-model="value" placeholder="检索类型">
            <el-option
              v-for="item in searchoptions"
              :key="item.value"
              :label="item.label"
              :value="item.value">
            </el-option>
         </el-select>
      </el-tooltip>
      <el-tooltip content="支持模糊搜索,空格分离多关键字" effect="dark" placement="bottom">
        <el-input @keyup.enter.native="handleSearch" prefix-icon="el-icon-search" v-model="input" placeholder="检索关键字" style="width: 200px;"  class="filter-item"></el-input>

      </el-tooltip>
       <el-button  v-waves class="filter-item" type="primary" icon="el-icon-search" @click="handleSearch" style="width: 140px" >
        搜索
      </el-button>
      <el-button  v-permission="['admin']"   class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-edit" @click="handleCreate">
        添加
      </el-button>

    </div>


     <el-table
         :data="list.slice((currentPage-1)*PageSize,currentPage*PageSize)"
         v-loading="loading"
         height="500"
         border
         style="width: 100%"
         :default-sort = "{prop: 'category', order: 'decreasing'}"

         >
         <el-table-column
               type="index"
               :index="indexMethod">
             </el-table-column>


         <el-table-column
           prop="bookName"
           label="书名"
           sortable
           width="180">
         </el-table-column>
         <el-table-column
           prop="author"
           label="作者"
           sortable
           width="180">
         </el-table-column>
         <el-table-column
           prop="publisher"
           sortable
           label="出版社">
         </el-table-column>
         <el-table-column
           prop="ISDN"
           sortable
           label="ISBN">
         </el-table-column>
         <el-table-column
           prop="category"
           sortable

           label="分类">
         </el-table-column>
         <el-table-column


           label="数量">
           <template slot-scope="scope">
               <p >{{parseInt(scope.row.num)}}</p>
               </template>
           </el-table-column>
         </el-table-column>
         <el-table-column
               fixed="right"
               label="操作"
               width="100"
               >
               <template slot-scope="scope">
                 <el-button @click="handleAppoint(scope.row)" type="text" size="small" v-permission="['user']">预约</el-button>
                 <el-button @click="handleEdit(scope.row)" type="text" size="small" v-permission="['admin']">编辑</el-button>
                 <el-button @click="handleDelete(scope.row)" type="text" size="small" v-permission="['admin']">删除</el-button>
               </template>
             </el-table-column>
       </el-table>

       <div class="tabListPage">
          <el-pagination @size-change="handleSizeChange"
                         @current-change="handleCurrentChange"
                         :current-page="currentPage"
                         :page-sizes="pageSizes"
                         :page-size="PageSize" layout="total, sizes, prev, pager, next, jumper"
                         :total="totalCount">
            </el-pagination>
      </div>

      <el-dialog title="添加图书" :visible.sync="dialogFormVisible" >
         <el-form :model="temp" ref="temp" :label-position="right" label-width="80px" :rules="rules">
           <el-form-item label="书名" prop="bookName">
             <el-input v-model="temp.bookName" />
           </el-form-item>
           <el-form-item label="作者" prop="author">
             <el-input v-model="temp.author" />
           </el-form-item>
           <el-form-item label="ISBN" prop="ISDN">
             <el-input v-model="temp.ISDN" />
           </el-form-item>
           <el-form-item label="出版社" prop="publisher">
             <el-input v-model="temp.publisher" />
           </el-form-item>
           <el-form-item label="分类" prop="category">
               <el-select v-model="temp.category" placeholder="请选择类别" style="width: 100%;">
                 <el-option
                       v-for="item in options"
                       :key="item.value"
                       :label="item.label"
                       :value="item.value">
                     </el-option>
               </el-select>
             </el-form-item>
           <el-form-item label="剩余数量" prop="num">
             <el-input v-model.number="temp.num" type="number"/>
           </el-form-item>
           <el-form-item >
               <el-button type="primary" @click="submitForm('temp')">立即创建</el-button>
               <el-button @click="resetForm('temp')">重置</el-button>
                <el-tooltip content="根据输入的ISBN自动获取图书信息" effect="dark" placement="bottom">
                <el-button type="success" @click="fastISBN('temp')">ISBN快速导入</el-button>
                </el-tooltip>
            </el-form-item>
         </el-form>

       </el-dialog>


       <el-dialog title="编辑图书" :visible.sync="editVisible" >
          <el-form :model="edit" ref="edit" :label-position="right" label-width="80px" :rules="rules">
            <el-form-item label="书名" prop="bookName">
              <el-input v-model="edit.bookName" />
            </el-form-item>
            <el-form-item label="作者" prop="author">
              <el-input v-model="edit.author" />
            </el-form-item>
            <el-tooltip content="不可以修改ISBN" effect="dark" placement="bottom">
              <el-form-item label="ISDN" prop="ISDN">
                <el-input v-model="edit.ISDN" :disabled="true"/>
              </el-form-item>
            </el-tooltip>

            <el-form-item label="出版社" prop="publisher">
              <el-input v-model="edit.publisher" />
            </el-form-item>
            <el-form-item label="分类" prop="category">
                <el-select v-model="edit.category" placeholder="请选择类别" style="width: 100%;">
                  <el-option
                        v-for="item in options"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                      </el-option>
                </el-select>
              </el-form-item>
            <el-form-item label="数量" prop="num">
              <el-input v-model.number="edit.num" type="number" :disabled="true"/>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="submitEdit('edit')">立即修改</el-button>
                <el-button @click="resetEdit('edit')">重置修改</el-button>
             </el-form-item>
          </el-form>

        </el-dialog>

  </div>
</template>

<script>
import permission from '@/directive/permission/index.js'
import axios from 'axios';
import gettoken from '../../../src/store/modules/user.js'
import store from '../../store/modules/user'
export default {
  name: 'ComplexTable',
  directives: { permission },
  filters: {

  },
  data() {
    var checkNum = (rule, value, callback) => {
            if (!value) {
              return callback(new Error('数量不能为空或小于等于0'));
            }
            setTimeout(() => {
              if (!Number.isInteger(value)) {
                callback(new Error('请输入数字值'));
              } else {
                if (value < 0) {
                  callback(new Error('数量必须大于0'));
                } else {
                  callback();
                }
              }
            }, 1000);
          };

    return {
       list:[],
       loading:false,
       userid:store.state.name,
       input: '',
       searchoptions: [{
                 value: 'bookName',
                 label: '书名'
               }, {
                 value: 'author',
                 label: '作者'
               }, {
                 value: 'ISDN',
                 label: 'ISDN'
               }, {
                 value: 'publisher',
                 label: '出版社'
               }
               ],
       options: [{
                 value: '艺术',
                 label: '艺术'
               }, {
                 value: '文学',
                 label: '文学'
               }, {
                 value: '自然学科',
                 label: '自然学科'
               }, {
                 value: '数理科学',
                 label: '数理科学'
               }
               ],
        value: 'bookName',
        words:null,
        dialogFormVisible:false,
        editVisible:false,
        temp:{
          bookName:'',
          author:'',
          ISDN:'',
          publisher:'',
          category:'',
          num:''
        },
        edit:{
          bookName:'',
          author:'',
          ISDN:'',
          publisher:'',
          category:'',
          num:''
        },
        resetEditMes:{
          bookName:'',
          author:'',
          ISDN:'',
          publisher:'',
          category:'',
          num:''
        },
         // 约束条件还没写完
        rules: {
            bookName: [
              { required: true, message: '请输入书名', trigger: 'blur' },
              { min: 1, max: 50, message: '长度在 1 到 50 个字符/中文', trigger: 'blur' }
            ],
            author: [
              { required: true, message: '请输入作者名', trigger: 'blur' },
              { min: 1, max: 50, message: '长度在 1 到 50 个字符/中文', trigger: 'blur' }
            ],
            ISDN: [
              { required: true, message: '请输入ISBN', trigger: 'blur' },
              { min: 13, max: 13, message: '长度在 13个字符', trigger: 'blur' },

            ],
            publisher: [
              { required: true, message: '请输入出版社', trigger: 'blur' },
              { min: 1, max: 50, message: '长度在 1 到 50 个字符/中文', trigger: 'blur' }
            ],
            category: [
              { required: true, message: '请输入分类', trigger: 'blur' },
              { min: 1, max: 10, message: '长度在 1 到 10 个字符', trigger: 'blur' }
            ],
            num: [

                { validator: checkNum, trigger: 'blur' }
            ]

          },


         // 默认显示第几页
         currentPage:1,
         // 总条数，根据接口获取数据长度
         totalCount:1,
         // 个数选择器
         pageSizes:[10,20,30,40],
         // 默认每页显示的条数（可修改）
         PageSize:10,
    }
  },
  created() {
    this.initList()

  },
  methods: {

    handleEdit(row) {

        this.edit.bookName=row.bookName;
        this.edit.author=row.author;
        this.edit.ISDN=row.ISDN;
        this.edit.publisher=row.publisher;
        this.edit.category=row.category;
        this.edit.num=Number(row.num);

        this.resetEditMes.bookName=row.bookName;
        this.resetEditMes.author=row.author;
        this.resetEditMes.ISDN=row.ISDN;
        this.resetEditMes.publisher=row.publisher;
        this.resetEditMes.category=row.category;
        this.resetEditMes.num=Number(row.num);
        this.editVisible=true

    },
    handleDelete(row) {
      var vm=this
        this.$confirm('此操作将永久删除《'+row.bookName+'》，确定吗', '提示', {
                  confirmButtonText: '确定',
                  cancelButtonText: '取消',
                  type: 'warning'
                }).then(() => {
                  axios.post('http://127.0.0.1:5000/api/deletebook', {
                     bookName:row.bookName,
                     author:row.author,
                     ISDN:row.ISDN,
                     publisher:row.publisher,
                     category:row.category,
                     num:row.num
                    })

                    .then(function (response) {
                    //  this.$refs[temp].resetFields();
                      vm.$message({
                          type: 'success',
                          message: '删除成功!'
                        });
                        
                    })
                    .catch(function (error) {
                      vm.$message({
                          type: 'info',
                          message: error
                        });
                  })

                  setTimeout(() => {
                    this.initList()
                  }, 1.5 * 1000)
                }).catch(() => {
                  this.$message({
                    type: 'info',
                    message: '已取消删除'
                  });
                });
    },
    handleAppoint(row) {
      var vm=this
      if(row.num<=0){
        vm.$message({
                type: 'error',
                message: '该书剩余量为0,无法预约!'
              });
      }else{

        this.$confirm('您要预约《'+row.bookName+'》，确定吗', '提示', {
                  confirmButtonText: '确定',
                  cancelButtonText: '取消',
                  type: 'info'
                }).then(() => {
                  axios.post('http://127.0.0.1:5000/api/regist', {
                     isdn:row.ISDN,
                     userid:vm.userid,
                     author:row.author,
                     bookname:row.bookName
                    })

                    .then(function (response) {
                    //  this.$refs[temp].resetFields();
                      if(response.data=='已经借阅'){
                        vm.$message({
                                type: 'error',
                                message: '您已借阅该本图书，请勿重复借阅'
                              });
                      }
                      else if(response.data=='已经预约'){
                        vm.$message({
                                type: 'error',
                                message: '您已经预约了改本图书，请勿重复预约'
                              });
                      }
                      else{
                        vm.$message({
                                type: 'success',
                                message: '预约成功!'
                              });
                      }
                      
                    })
                    .catch(function (error) {
                      vm.$message({
                          type: 'info',
                          message: error
                        });
                  })

                  setTimeout(() => {
                    this.initList()
                  }, 1.5 * 1000)
                }).catch(() => {
                  this.$message({
                    type: 'info',
                    message: '已取消删除'
                  });
                });
      }

    },
    initList(){
      var vm=this
      this.loading=true;
      const path = 'http://127.0.0.1:5000/api/books';
            axios.get(path)
              .then((res) => {
                this.list = res.data;
                this.loading=false
                this.totalCount=Object.keys(this.list).length
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
    getList() {
      var vm=this
      this.loading=true;
      const path = 'http://127.0.0.1:5000/api/books/search';
            axios.post(path, {
               words:vm.words,
               type:vm.value
              })

              .then(function (response) {
              //  this.$refs[temp].resetFields();
                 vm.list=response.data
                 vm.loading=false
                 vm.totalCount=Object.keys(vm.list).length
                
              })
              .catch(function (error) {
                 vm.$message({
                    type: 'info',
                    message: '查询失败'+error
                  });
                   vm.loading=false
            })


    },
    handleCreate() {

      this.dialogFormVisible = true

    },
     // 每页显示的条数
     handleSizeChange(val) {
         // 改变每页显示的条数
         this.PageSize=val
         // 注意：在改变每页显示的条数时，要将页码显示到第一页
         this.currentPage=1
     },
       // 显示第几页
     handleCurrentChange(val) {
         // 改变默认的页数
         this.currentPage=val
     },
     handleSearch(){

       if(this.input==''){

         this.initList()

       }else{
         this.words=this.input
         this.getList()
       }

     },

     submitForm(formName) {
         var vm = this;
         let mytoken=gettoken.state.token
         this.$refs[formName].validate((valid) => {
           if (valid) {
             axios.post('http://127.0.0.1:5000/api/addbook', {
                bookName:this.temp.bookName,
                author:this.temp.author,
                ISDN:this.temp.ISDN,
                publisher:this.temp.publisher,
                category:this.temp.category,
                num:this.temp.num,
                token:mytoken
               })

               .then(function (response) {
                 // this.$refs[formName].resetFields();
                 vm.$message({
                      message: '添加成功',
                      type: 'success'
                  });

               })
               .catch(function (error) {
                  vm.$message({
                       showClose: true,
                       message:'出错啦！您输入的ISDN已经存在或网络异常',
                       type: 'warning'
                     });
                })
               setTimeout(() => {
                 this.initList()
               }, 1.5 * 1000)
           } else {
             this.$message({
                       showClose: true,
                       message: '您的输入不合法，提交失败，请检查后重新提交',
                       type: 'warning'
                     });
             return false;
           }
         });
       },
       resetForm(formName) {
         this.$refs[formName].resetFields();
       },
       submitEdit(formName) {
           var vm=this
           let mytoken=gettoken.state.token
           this.$refs[formName].validate((valid) => {

             if (valid) {
               this.$confirm('此修改操作不可逆, 是否继续', '提示', {
                         confirmButtonText: '确定',
                         cancelButtonText: '取消',
                         type: 'warning'
                       }).then(() => {
                         axios.post('http://127.0.0.1:5000/api/editbook', {
                            bookName:this.edit.bookName,
                            author:this.edit.author,
                            ISDN:this.edit.ISDN,
                            publisher:this.edit.publisher,
                            category:this.edit.category,
                            num:this.edit.num,
                            token:mytoken
                           })

                           .then(function (response) {

                             vm.$message({
                               type: 'success',
                               message: '修改成功!'
                             });
                             vm.editVisible=false
                           })
                           .catch(function (error) {
                             vm.$message({
                                 type: 'info',
                                 message: '修改出现异常'
                               });
                            })
                           setTimeout(() => {
                             vm.initList()
                           }, 1.5 * 1000)

                       }).catch(() => {
                         vm.$message({
                           type: 'info',
                           message: '已取消删除'
                         });
               });

             } else {
               this.$message({
                         showClose: true,
                         message: '您的输入不合法，提交失败，请检查后重新提交',
                         type: 'warning'
                       });
               return false;
             }
           });
         },
         resetEdit(formName) {
           this.edit.bookName=this.resetEditMes.bookName;
           this.edit.author=this.resetEditMes.author;
           this.edit.ISDN=this.resetEditMes.ISDN;
           this.edit.publisher=this.resetEditMes.publisher;
           this.edit.category=this.resetEditMes.category;
           this.edit.num=this.resetEditMes.num;
         },
         sortByDate(obj1, obj2) {
              if(obj1.category==obj2.category){
                let val1 = obj1.num
                let val2 = obj2.num
                return val1 - val2
              }

         },
         fastISBN(data){
           var vm=this

           const path = '/fast/isbn/'+ vm.temp.ISDN ;
                 axios.get(path)
                   .then((res) => {
                     // this.list = res.data;
                     // this.loading=false
                     // this.totalCount=Object.keys(this.list).length
                      vm.temp.bookName=res.data.title
                      vm.temp.author=res.data.book_info.作者
                      vm.temp.publisher=res.data.book_info.出版社

                   })
                   .catch((error) => {
                     // eslint-disable-next-line
                     vm.$message({
                             type: 'info',
                             message: '获取数据失败了'
                     });

                   });
         }




    },
    }
</script>
