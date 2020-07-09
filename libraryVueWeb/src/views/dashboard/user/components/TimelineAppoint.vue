<template>
  <div class="block">
    <el-timeline>
      <el-timeline-item v-for="(item,index) of datalist" :key="index" :timestamp="item.opertime" :reverse="true" placement="top">
        <el-card>
          <h4>书名：{{ item.bookname }}</h4>
          <p>作者：{{ item.author }}</p>
          <p>ISBN：{{ item.bookisdn }}</p>
           <p>预约时间：{{ item.opertime }}</p>
        </el-card>
      </el-timeline-item>
    </el-timeline>
  </div>
</template>

<script>
import store from '../../../../store/modules/user.js';
import axios from 'axios';
export default {
  data() {
    return {
	  userid:store.state.name,
	  totalCount:0,
    datalist: '',
    }
  },
  created() {

    this.getAppintList();

  },
  methods:{
	  getAppintList(){
		  var vm=store.state.name
      this.userid=
		  this.loading=true;
		  const path = 'http://127.0.0.1:5000/api/myapplist';
		        axios.get(path,{params:{userid:store.state.name}})
		          .then((res) => {
		            this.datalist = res.data;
		            this.totalCount=Object.keys(this.list).length
		          })
		          .catch((error) => {
		            // eslint-disable-next-line
		            vm.$message({
		                    type: 'info',
		                    message: '出错啦！获取预约书单失败'
		            });

		          });
	  }
  }
}
</script>
