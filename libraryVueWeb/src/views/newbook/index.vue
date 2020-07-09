<template>
  <div class="tab-container">
   <h1>新到图书</h1>
    <el-tabs v-model="activeName" style="margin-top:15px;" type="border-card">
      <el-tab-pane v-for="item in tabMapOptions" :key="item.key" :label="item.label" :name="item.key">
        <keep-alive>
          <tab-pane v-if="activeName==item.key" :type="item.key" @create="showCreatedTimes" />
        </keep-alive>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
import tabPane from './components/TabPane'

export default {
  name: 'Tab',
  components: { tabPane },
  data() {
    return {
      tabMapOptions: [
        { label: '新到书籍', key: 'BOOK' },
        // { label: '新到期刊', key: 'MAG' },

      ],
      activeName: 'BOOK',
    }
  },
  watch: {
    activeName(val) {
      this.$router.push(`${this.$route.path}?tab=${val}`)
    }
  },
  created() {
    // init the default selected tab
    // const tab = this.$route.query.tab
    if (tab) {
      this.activeName = tab
    }
  },
  methods: {
    
  }
}
</script>

<style scoped>
  .tab-container {
    margin: 30px;
  }
</style>
