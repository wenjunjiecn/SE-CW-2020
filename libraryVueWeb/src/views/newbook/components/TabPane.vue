<template>
  <el-table  v-el-table-infinite-scroll="load"   lazy='true' v-loading="listLoading" :data="list" border fit highlight-current-row style="width: 100%" height='auto/100%'>
    <el-table-column
          prop="bookName"
          label="书名"
          width="180">

        </el-table-column>
        <el-table-column
          prop="author"
          label="作者"
          width="180">
        </el-table-column>
        <el-table-column
          prop="publisher"
          label="出版社">
        </el-table-column>
        <el-table-column
          prop="addtime"
          label="到书时间">
        </el-table-column>


  </el-table>

</template>

<script>
import { fetchList } from '@/api/article'
import axios from 'axios';
import elTableInfiniteScroll from 'el-table-infinite-scroll';
export default {
  directives: {
      'el-table-infinite-scroll': elTableInfiniteScroll
    },
  data() {
    return {
      pageIndex:1,
      list: [],

      loading: false,
      listLoading:true
    }
  },
  created() {
    this.getList()
    this.pageIndex=this.pageIndex+1
  },
  methods: {
    getList() {
      var vm=this
      this.loading=false;
      const path = 'http://127.0.0.1:5000/api/newbooks';
            axios.get(path,{
              params: {
                  pageIndex: vm.pageIndex,
              }
            })
              .then((res) => {

                if ( res.data != 0){
                  vm.pageIndex=vm.pageIndex+1;
                  vm.list = vm.list.concat( res.data) ;
                  vm.loading=false;
                  vm.listLoading=false
                  vm.$message({
                          type: 'success',
                          message: '加载数据成功'
                        });
                }
                else{
                  this.$message.success('无更多数据');
                }
              })
              .catch((error) => {
                // eslint-disable-next-line
                console.error('出错啦！获取数据失败');
                vm.loading=false;
                vm.listLoading=false
              });

    },
    load() {
          // this.$message.success('加载下一页');
          this.getList();
    }
  }
}
</script>
