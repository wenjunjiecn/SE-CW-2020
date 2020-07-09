<template>
  <div class="app-container">
    <div v-if="user">
      <el-row :gutter="20">

        <el-col :span="9" :xs="24">
          <user-card :user="user" />
           <info-card />
        </el-col>


       <el-col :span="15" :xs="24">
          <el-card>
            <el-tabs v-model="activeTab">
              <el-tab-pane label="当前借阅图书" name="借阅图书">
                 <timeline />
              </el-tab-pane>
              <el-tab-pane label="当前预约图书" name="预约图书">
                  <timeline2 />
              </el-tab-pane>

            </el-tabs>
          </el-card>
        </el-col>

      </el-row>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import UserCard from './components/UserCard'
import Activity from './components/Activity'
import Timeline from './components/Timeline'
import Timeline2 from './components/TimelineAppoint'
import InfoCard from './components/Infocard'

export default {
  name: 'Profile',
  components: { UserCard, Activity, Timeline,Timeline2,InfoCard},
  data() {
    return {
      user: {},
      activeTab: '借阅图书'
    }
  },
  computed: {
    ...mapGetters([
      'name',
      'avatar',
      'roles'
    ])
  },
  created() {
    this.getUser()
  },
  methods: {
    getUser() {
      this.user = {
        name: this.name,
        role: this.roles.join(' | '),
        email: '123@ncepu.edu.cn',
        avatar: this.avatar
      }
    }

  }
}
</script>
