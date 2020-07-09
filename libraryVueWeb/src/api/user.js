import request from '@/utils/request'

export function login(data) {
  return request({
    url: '/api/login',
    // url: '/user/login',
    method: 'post',
    data
  })
}

export function getInfo(token) {
  return request({
    // url: '/api/userinfo',
    url: '/api/user/info',
    method: 'get',
    params: { token }
  })
}

export function logout(data) {
  return request({
    url: 'http://127.0.0.1:5000/api/user/logout',
    // url: 'api/user/logout',
    method: 'post',
   data
  })
}
