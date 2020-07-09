<template>
  <div class="dashboard-editor-container">
    <!-- 用户卡片 -->
    <el-row :gutter="8">
      <el-col :xs="{span: 24}" :sm="{span: 12}" :md="{span: 12}" :lg="{span: 6}" :xl="{span: 6}" style="margin-bottom:170px;">
        <box-card />
      </el-col>

      
    </el-row>
    

  </div>
</template>

<script>

import BoxCard from './components/BoxCard'
import {ceshi} from '@/api/test.js'
import axios from 'axios';

export default {
  name: 'DashboardAdmin',
  components: {
    BoxCard
  },
  data() {
    return {
	    books:[]
    }
  },
  methods: {
    getBooks() {
          const path = 'http://localhost:5000/books';
          axios.get(path)
            .then((res) => {
              this.books = res.data.books;
            })
            .catch((error) => {
              // eslint-disable-next-line
              console.error(error);
            });
        },
    ceshia(){
       this.list='111111111111'
	    ceshi().then(res=>{
  		    this.list=res.data.list
	    })
    },
    handleSetLineChartData(type) {
      this.lineChartData = lineChartData[type]
    }
  }
}
</script>

<style lang="scss" scoped>
.dashboard-editor-container {
  padding: 32px;
  background-color: rgb(240, 242, 245);
  position: relative;


  .chart-wrapper {
    background: #fff;
    padding: 16px 16px 0;
    margin-bottom: 32px;
  }
}

@media (max-width:1024px) {
  .chart-wrapper {
    padding: 8px;
  }
}
</style>
