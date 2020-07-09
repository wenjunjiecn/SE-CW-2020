<template>
  <div class="createPost-container"  >
    <h3 style="text-align: center;margin-top: 12.5rem ;" v-permission="['admin']">尊敬的管理员，发布留言功能仅提供给读者使用，去别处看看吧</h3>
    <el-form ref="postForm" :model="postForm" :rules="rules" class="form-container" v-permission="['user']">

      <sticky :z-index="10" :class-name="'sub-navbar '+postForm.status">
        <el-button v-loading="loading" style="margin-left: 10px;" type="success" @click="submitForm">
          发布
        </el-button>
      </sticky>

      <div class="createPost-main-container">
        <el-row>
          <!-- <Warning /> -->
          <h1>发布留言</h1>
          <el-tooltip content="学号默认填入,不可修改" effect="dark" placement="bottom">
            <el-form-item label-width="60px" label="学号:" class="postInfo-container-item" prop="id"  style="width: 230px;">
              <el-input v-model="postForm.id" placeholder="请输入学号" disabled="true"></el-input>
            </el-form-item>
          </el-tooltip>

          <el-form-item prop="content" style="margin-bottom: 30px;" height="400px">
            <p style="margin: 0 ;padding: 0; color:grey">已输入{{postForm.content.length}}字符，注意不要超过200字</p>
            <el-input
              type="textarea"
              :rows="10"
              placeholder="请输入留言内容"
              :max="200"
              v-model="postForm.content">
            </el-input>
          </el-form-item>
        </el-row>







      </div>
    </el-form>
  </div>
</template>

<script>

import Sticky from '@/components/Sticky' // 粘性header组件
import store from '../../../store/modules/user'
import permission from '@/directive/permission/index.js' // 权限判断指令
import axios from 'axios';
const defaultForm = {
  status: 'draft',
  id:store.state.name,
  content: '', // 文章内容

}

export default {
  name: 'ArticleDetail',
  components: { Sticky},
  props: {
    isEdit: {
      type: Boolean,
      default: false
    }
  },
 directives: { permission },
  data() {
    return{
      postForm:{
        status: 'draft',
        id:store.state.name,
        content: '', // 文章内容
      },
      rules: {

        content: [
           // { max: 500, message: '最多不超过500个字符', trigger: 'blur' }
            {required: true, message: '请输入留言内容', trigger: 'blur' },
            { min: 2, max: 200, message: '长度在 2 到 200 个字符(包含汉字)', trigger: 'blur' }
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
          const path = 'http://127.0.0.1:5000/api/message/publish';
                axios.post(path, {
                   content:vm.postForm.content,
                   readID:vm.postForm.id,

                  })

                  .then(function (response) {
                  //  this.$refs[temp].resetFields();
                   
                      vm.$notify({
                        title: '成功',
                        message: '发布留言成功',
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
