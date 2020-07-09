import request from '@/utils/request'

export function ceshi(){
      return request({
        url:'/test',
        method:'get'
      })
}
