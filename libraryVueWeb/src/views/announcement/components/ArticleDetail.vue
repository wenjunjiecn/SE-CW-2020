<template>
  <div class="createPost-container">
    <el-form ref="postForm" :model="postForm" :rules="rules" class="form-container">

      <sticky :z-index="10" :class-name="'sub-navbar '+postForm.status">
        <el-button v-loading="loading" style="margin-left: 10px;" type="success" @click="submitForm">
          发布
        </el-button>

      </sticky>

      <div class="createPost-main-container">
        <el-row>
          <!-- <Warning /> -->
          <h1>发布公告</h1>
          <el-col :span="24">
            <el-form-item style="margin-bottom: 40px;" prop="title">
              <MDinput v-model="postForm.title" :maxlength="100" name="name" required>
                标题
              </MDinput>
            </el-form-item>

            <div class="postInfo-container">
              <el-row>
                <el-col :span="8">
                  <el-form-item label-width="60px" label="作者:" class="postInfo-container-item" prop="author">
                    <el-input v-model="postForm.author" placeholder="请输入作者"></el-input>
                  </el-form-item>
                </el-col>

                <el-col :span="10">
                  <el-form-item label-width="120px" label="发布时间:" class="postInfo-container-item" prop="display_time" >
                    <el-date-picker v-model="postForm.display_time" type="datetime"  format="yyyy-MM-dd HH:mm:ss" placeholder="选择一个发布时间" />
                  </el-form-item>
                </el-col>

                <el-col :span="6">
                  <el-form-item label-width="90px" label="优先级:" class="postInfo-container-item" prop="important" >
                    <el-rate
                      v-model="postForm.importance"
                      :max="3"
                      :colors="['#99A9BF', '#F7BA2A', '#FF9900']"
                      :low-threshold="1"
                      :high-threshold="3"
                      style="display:inline-block"
                    />
                  </el-form-item>
                </el-col>
              </el-row>
            </div>
          </el-col>
        </el-row>

        <el-form-item style="margin-bottom: 40px;" label-width="70px" label="摘要:" prop="content_short">
          <el-input v-model="postForm.content_short" :rows="1" type="textarea" class="article-textarea" autosize placeholder="请输入内容" />
          <span v-show="contentShortLength" class="word-counter">{{ contentShortLength }}words</span>
        </el-form-item>
        <p style="margin: 0 ;padding: 0; color:grey">目前生成的html文件长度为:{{postForm.content.length}}字符，请注意不要超过2000</p>
        <el-form-item prop="content" style="margin-bottom: 30px;">

          <Tinymce ref="editor" v-model="postForm.content" :height="400" />

        </el-form-item>


      </div>
    </el-form>
  </div>
</template>

<script>
import Tinymce from '@/components/Tinymce'
import Upload from '@/components/Upload/SingleImage3'
import MDinput from '@/components/MDinput'
import Sticky from '@/components/Sticky' // 粘性header组件
import { validURL } from '@/utils/validate'
import { fetchArticle } from '@/api/article'
import store from '../../../store/modules/user.js'
import Warning from './Warning'
import { CommentDropdown, PlatformDropdown, SourceUrlDropdown } from './Dropdown'
import axios from 'axios';

const defaultForm = {
  status: 'draft',
  title: '', // 文章题目
  content: '', // 文章内容
  content_short: '', // 文章摘要
  display_time: undefined, // 前台展示时间
  id: undefined,
  importance: 0
}

export default {
  name: 'ArticleDetail',
  components: { Tinymce, MDinput, Upload, Sticky, Warning, CommentDropdown, PlatformDropdown, SourceUrlDropdown },
  props: {
    isEdit: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return{
      postForm:{
        status: 'draft',
        title: '', // 文章题目
        content: '', // 文章内容
        content_short: '', // 文章摘要
        display_time: undefined, // 前台展示时间
        importance: 0,
        author:''
      },
      rules: {
        title: [
            { required: true, message: '请输入标题', trigger: 'blur' },
            { min: 2, max: 30, message: '长度在 2 到 30 个字符（包括汉字）', trigger: 'blur' }
          ],
        content: [
           // { max: 500, message: '最多不超过500个字符', trigger: 'blur' }
            {required: true, message: '请输入发布内容', trigger: 'blur' },
            { min: 2, max: 2000, message: '生成的html长度在 2 到 2000 个字符', trigger: 'blur' }
        ],
        content_short: [
            { required: true, message: '请输入概要', trigger: 'blur' },
            { min: 2, max: 250, message: '长度在 2 到 250 个字符（包括汉字）', trigger: 'blur' }
          ],
        author: [
            { required: true, message: '请输入作者', trigger: 'blur' },
            { min: 1, max: 12, message: '长度在 1 到 12 个字符（包括汉字）', trigger: 'blur' }
          ],
        display_time: [
            { required: true, message: '请选择时间', trigger: 'blur' },

          ],
        important: [

        ],
      },
    }

  },

  methods: {

    submitForm() {
      var vm=this
      console.log(this.postForm)
      this.$refs.postForm.validate(valid => {
        if (valid) {
          self=this
          const path = 'http://127.0.0.1:5000/api/announcement/publish';
                axios.post(path, {
                   title:vm.postForm.title,
                   content:vm.postForm.content,
                   content_short:vm.postForm.content_short,
                   time:this.moment(vm.postForm.display_time).format("YYYY-MM-DD HH:mm:ss"),
                   importance:vm.postForm.importance,
                   author:vm.postForm.author,
                   adminID:store.state.name
                  })

                  .then(function (response) {
                  //  this.$refs[temp].resetFields();
                   
                      vm.$notify({
                        title: '成功',
                        message: '发布文章成功',
                        type: 'success',
                        duration: 2000,

                      })
                      vm.postForm.status = 'published'
                      self.loading = false
                  })
                  .catch(function (error) {
                     vm.$message({
                        type: 'info',
                        message: '发布失败'
                      });

                })
             this.loading = false
        } else {
          vm.$message({
                  type: 'info',
                  message: '发布失败，请检查输入是否完整'
           });
        }
      })
    },


  }
}
</script>







<style lang="scss" scoped>
@import "~@/styles/mixin.scss";

.createPost-container {
  position: relative;

  .createPost-main-container {
    padding: 40px 45px 20px 50px;

    .postInfo-container {
      position: relative;
      @include clearfix;
      margin-bottom: 10px;

      .postInfo-container-item {
        float: left;
      }
    }
  }

  .word-counter {
    width: 40px;
    position: absolute;
    right: 10px;
    top: 0px;
  }
}

.article-textarea /deep/ {
  textarea {
    padding-right: 40px;
    resize: none;
    border: none;
    border-radius: 0px;
    border-bottom: 1px solid #bfcbd9;
  }
}
</style>
