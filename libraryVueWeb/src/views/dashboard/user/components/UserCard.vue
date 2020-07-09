<template>
  <el-card style="margin-bottom:20px;">
    <div slot="header" class="clearfix">
      <span>亲爱的读者，欢迎您</span>
    </div>

    <div class="user-profile">
      <div class="box-center">
        <pan-thumb image="https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1573283138&di=933c5cf8f4882043a5fa568006479945&src=http://d.hiphotos.baidu.com/zhidao/pic/item/8644ebf81a4c510f9a4fd0266359252dd42aa506.jpg" :height="'100px'" :width="'100px'" :hoverable="false">
        </pan-thumb>
      </div>
      <div class="box-center">
        <div class="user-name text-center">你好</div>
        <div class="user-role text-center text-muted">{{name}}</div>
      </div>
    </div>
    </div>
  </el-card>
</template>

<script>
import PanThumb from '@/components/PanThumb'
import store from '../../../../store/modules/user.js'
export default {
  components: { PanThumb },
  data(){
    return{
      name:store.state.name
    }
  },
  props: {
    user: {
      type: Object,
      default: () => {
        return {
          name:'',
          email: '',
          avatar: '',
          roles: '用户类型'
        }
      }
    }
  }
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

 .user-profile {
   .user-name {
     font-weight: bold;
   }

   .box-center {
     padding-top: 10px;
   }

   .user-role {
     padding-top: 10px;
     font-weight: 400;
     font-size: 14px;
   }

   .box-social {
     padding-top: 30px;

     .el-table {
       border-top: 1px solid #dfe6ec;
     }
   }

   .user-follow {
     padding-top: 20px;
   }
 }

 .user-bio {
   margin-top: 20px;
   color: #606266;

   span {
     padding-left: 4px;
   }

   .user-bio-section {
     font-size: 14px;
     padding: 15px 0;

     .user-bio-section-header {
       border-bottom: 1px solid #dfe6ec;
       padding-bottom: 10px;
       margin-bottom: 10px;
       font-weight: bold;
     }
   }
 }
</style>
