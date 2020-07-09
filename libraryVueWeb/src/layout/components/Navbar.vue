<template>
  <div class="navbar">
    <el-tooltip content="缩放边栏" effect="dark" placement="bottom">
       <hamburger id="hamburger-container" :is-active="sidebar.opened" class="hamburger-container" @toggleClick="toggleSideBar" />
    </el-tooltip>
    <breadcrumb id="breadcrumb-container" class="breadcrumb-container" />

    <div class="right-menu">
      <template v-if="device!=='mobile'">
        <el-tooltip content="功能搜索" effect="dark" placement="bottom">
            <search id="header-search" class="right-menu-item" />
        </el-tooltip>


        <error-log class="errLog-container right-menu-item hover-effect" />
        <el-tooltip content="系统使用引导" effect="dark" placement="bottom">
          <div  class="right-menu-item hover-effect"  @click.prevent.stop="guide">  <svg-icon icon-class="guide"/> </div>
        </el-tooltip>
        <el-tooltip content="全屏显示" effect="dark" placement="bottom">
          <screenfull id="screenfull" class="right-menu-item hover-effect" />
        </el-tooltip>
        <!-- <el-tooltip content="字体设置" effect="dark" placement="bottom">
          <size-select id="size-select" class="right-menu-item hover-effect" />
        </el-tooltip> -->

      </template>

      <el-dropdown class="avatar-container right-menu-item hover-effect" trigger="click">
        <el-tooltip content="主页/退出登录" effect="dark" placement="bottom">
          <div class="avatar-wrapper">
            <img src="https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1573283138&di=933c5cf8f4882043a5fa568006479945&src=http://d.hiphotos.baidu.com/zhidao/pic/item/8644ebf81a4c510f9a4fd0266359252dd42aa506.jpg" class="user-avatar">

            <i class="el-icon-caret-bottom" />
          </div>
        </el-tooltip>

        <el-dropdown-menu slot="dropdown">
          <router-link to="/home">
            <el-dropdown-item>个人主页</el-dropdown-item>
          </router-link>
          <el-dropdown-item divided>
            <span style="display:block;" @click="logout">退出账户</span>
          </el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import Breadcrumb from '@/components/Breadcrumb'
import Hamburger from '@/components/Hamburger'
import ErrorLog from '@/components/ErrorLog'
import Screenfull from '@/components/Screenfull'
import SizeSelect from '@/components/SizeSelect'
import Search from '@/components/HeaderSearch'

import Driver from 'driver.js' // import driver.js
import 'driver.js/dist/driver.min.css' // import driver.js css
import steps from './steps'
import store from '../../store/modules/user.js'
export default {
  components: {
    Breadcrumb,
    Hamburger,
    ErrorLog,
    Screenfull,
    SizeSelect,
    Search
  },
  computed: {
    ...mapGetters([
      'sidebar',
      'avatar',
      'device'
    ])
  },
  methods: {
    toggleSideBar() {
      this.$store.dispatch('app/toggleSideBar')
    },
    async logout() {
      await this.$store.dispatch('user/logout')
      this.$router.push(`/login?redirect=${this.$route.fullPath}`)
    },
    guide() {
      this.driver = new Driver()
      this.driver.defineSteps(steps)
      this.driver.start()
    }
  }
}
</script>

<style lang="scss" scoped>
.navbar {
  height: 50px;
  overflow: hidden;
  position: relative;
  background: #fff;
  box-shadow: 0 1px 4px rgba(0,21,41,.08);

  .hamburger-container {
    line-height: 46px;
    height: 100%;
    float: left;
    cursor: pointer;
    transition: background .3s;
    -webkit-tap-highlight-color:transparent;

    &:hover {
      background: rgba(0, 0, 0, .025)
    }
  }

  .breadcrumb-container {
    float: left;
  }

  .errLog-container {
    display: inline-block;
    vertical-align: top;
  }

  .right-menu {
    float: right;
    height: 100%;
    line-height: 50px;

    &:focus {
      outline: none;
    }

    .right-menu-item {
      display: inline-block;
      padding: 0 8px;
      height: 100%;
      font-size: 18px;
      color: #5a5e66;
      vertical-align: text-bottom;

      &.hover-effect {
        cursor: pointer;
        transition: background .3s;

        &:hover {
          background: rgba(0, 0, 0, .025)
        }
      }
    }

    .avatar-container {
      margin-right: 30px;

      .avatar-wrapper {
        margin-top: 5px;
        position: relative;

        .user-avatar {
          cursor: pointer;
          width: 40px;
          height: 40px;
          border-radius: 10px;
        }

        .el-icon-caret-bottom {
          cursor: pointer;
          position: absolute;
          right: -20px;
          top: 25px;
          font-size: 12px;
        }
      }
    }
  }
}
</style>
