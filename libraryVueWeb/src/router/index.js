import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/layout'



/**
 * Note: sub-menu only appear when route children.length >= 1
 * Detail see: https://panjiachen.github.io/vue-element-admin-site/guide/essentials/router-and-nav.html
 *
 * hidden: true                   if set true, item will not show in the sidebar(default is false)
 * alwaysShow: true               if set true, will always show the root menu
 *                                if not set alwaysShow, when item has more than one children route,
 *                                it will becomes nested mode, otherwise not show the root menu
 * redirect: noRedirect           if set noRedirect will no redirect in the breadcrumb
 * name:'router-name'             the name is used by <keep-alive> (must set!!!)
 * meta : {
    roles: ['admin','editor']    control the page roles (you can set multiple roles)
    title: 'title'               the name show in sidebar and breadcrumb (recommend set)
    icon: 'svg-name'             the icon show in the sidebar
    noCache: true                if set true, the page will no be cached(default is false)
    affix: true                  if set true, the tag will affix in the tags-view
    breadcrumb: false            if set false, the item will hidden in breadcrumb(default is true)
    activeMenu: '/example/list'  if set path, the sidebar will highlight the path you set
  }
 */

/**
 * constantRoutes
 * a base page that does not have permission requirements
 * all roles can be accessed
 */
export const constantRoutes = [
  {
    path: '/redirect',
    component: Layout,
    hidden: true,
    children: [
      {
        path: '/redirect/:path*',
        component: () => import('@/views/redirect/index')
      }
    ]
  },
  {
    path: '/login',
    component: () => import('@/views/login/index'),
    hidden: true
  },
  {
    path: '/auth-redirect',
    component: () => import('@/views/login/auth-redirect'),
    hidden: true
  },
  {
    path: '/404',
    component: () => import('@/views/error-page/404'),
    hidden: true
  },
  {
    path: '/401',
    component: () => import('@/views/error-page/401'),
    hidden: true
  },
  // {
  //   path: '/',
  //   component: Layout,
  //   redirect: '/home',
  //   children: [
  //     {
  //       path: 'home',
  //       component: () => import('@/views/dashboard/index'),
  //       name: 'Home',
  //       meta: { title: '用户主页', icon: 'user', affix: true }
  //     }
  //   ]
  // },

]

/**
 * asyncRoutes
 * the routes that need to be dynamically loaded based on user roles
 */
export const asyncRoutes = [
  {
    path: '/',
    component: Layout,
    redirect: '/home',
    children: [
      {

        path: 'home',
        component: () => import('@/views/dashboard/index'),
        name: 'Home',
        meta: {  title: '用户主页', icon: 'user', affix: true }
      }
    ]
  },

  {
    path: '/search',
    component: Layout,
    children: [
      {

        path: '/search',
        component: () => import('@/views/search/index'),
        name: 'search',
        meta: {title: '查询图书期刊', icon: 'search' }
      }
    ]
  },
  {
    path: '/registlist',
    component: Layout,
    children: [
      {

        path: '/registlist',
        component: () => import('@/views/registlist/export-excel'),
        name: 'registlist',
        meta: {title: '预约登记表', icon: 'form',roles: ['admin'] }
      }
    ]
  },
  {
    path: '/borrowlist',
    component: Layout,
    children: [
      {

        path: '/borrowlist',
        component: () => import('@/views/borrowlist/export-excel'),
        name: 'borrowlist',
        meta: {title: '借阅信息表', icon: 'documentation',roles: ['admin'] }
      }
    ]
  },
  {
    path: '/announcement',
    component: Layout,
    redirect: '/announcement/list',
    name: 'Announcement',
    meta: {
      title: '公告',
      icon: 'announcement' ,role: ['admin'],
      hidden: true
    },
    children: [
      {
        path: 'create',
        component: () => import('@/views/announcement/create'),
        name: 'CreateAnnouce',
        meta: { roles:['admin'],title: '发布公告', icon: 'edit' }
      },
      {
        path: 'list',
        component: () => import('@/views/announcement/list'),
        name: 'AnnouceList',
        meta: { title: '查看公告', icon: 'annoucelist' }
      }
    ]
  },
  {
    path: '/message',
    component: Layout,
    redirect: '/message/list',
    name: 'Message',
    meta: {
      title: '读者留言',
      icon: 'message'
    },
    children: [
      {
        path: 'create',
        component: () => import('@/views/message/create'),
        name: 'CreateMessage',
        meta: {roles:['user'], title: '写留言', icon: 'edit' }
      },
      {
        path: 'list',
        component: () => import('@/views/message/list'),
        name: 'MessageList',
        meta: {roles:['admin'], title: '查看留言', icon: 'mesboard' }
      }
    ]
  },
  {
    path: '/newbook',
    component: Layout,
    children: [
      {
        path: 'index',
        component: () => import('@/views/newbook/index'),
        name: 'newbook',
        meta: { title: '新到图书', icon: 'new', hidden: true }
      }
    ]
  },
  {
    path: '/guide',
    component: Layout,
    children: [
      {
        path: 'index',
        component: () => import('@/views/guide/index'),
        name: 'guide',
        meta: { title: '系统使用引导', icon: 'guide',role: ['admin']}
      }
    ]
  },

  // 404 page must be placed at the end !!!
  { path: '*', redirect: '/404', hidden: true }
]

const createRouter = () => new Router({
  mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRoutes
})

const router = createRouter()

// Detail see: https://github.com/vuejs/vue-router/issues/1234#issuecomment-357941465
export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}

export default router
