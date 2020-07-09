<template>
  <div style="display:inline-block;">
    <label class="radio-label" style="padding-left:0;">导出文件名: </label>
    <el-input v-model="filename" placeholder="输入文件名 (默认:预约信息)" style="width:345px;" prefix-icon="el-icon-document" />
  </div>
</template>

<script>
export default {
  props: {
    value: {
      type: String,
      default: '预约信息'
    }
  },
  computed: {
    filename: {
      get() {
        return this.value
      },
      set(val) {
        this.$emit('input', val)
      }
    }
  }
}
</script>
