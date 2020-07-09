<template>
  <div class="app-container">
    <h1>查看留言</h1>
    <el-row>
      <el-col :span="24" :xs="24" justify="center" >
               <el-card>
                 <el-tabs v-model="activeTab">
                     <timeline />
                 </el-tabs>
               </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import Timeline from './components/Timeline'
export default {
   components: {  Timeline},
  data() {
    return {
      count: 600,
      loading: false
    }
  },
  computed: {
      noMore () {
        return this.count >= 20
      },
      disabled () {
        return this.loading || this.noMore
      }
   },
  created() {
    this.getList()
  },
  methods: {
    getList() {

    },
    load () {
            this.loading = true
            setTimeout(() => {
              this.count += 2
              this.loading = false
            }, 2000)
          }
  }
}
</script>

<style scoped>
.edit-input {
  padding-right: 100px;
}
.cancel-btn {
  position: absolute;
  right: 15px;
  top: 10px;
}
</style>
<style>
  .text {
    font-size: 14px;
  }

  .item {
    padding: 18px 0;
  }

  .box-card {
    width: 480px;
  }
</style>
