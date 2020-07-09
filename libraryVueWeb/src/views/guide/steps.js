const steps = [
  {
    element: '#hamburger-container',
    popover: {
      title: '手把手教你使用',
      description: '点击这里可以缩放侧边导航栏',
      position: 'bottom'
    }
  },
  {
    element: '#breadcrumb-container',
    popover: {
      title: '页面路径',
      description: '这里指示页面路径',
      position: 'bottom'
    }
  },
  {
    element: '#header-search',
    popover: {
      title: '搜索按钮',
      description: '这里可以快速搜索你想要的图书哦',
      position: 'left'
    }
  },
  {
    element: '#screenfull',
    popover: {
      title: '还可以全屏显示',
      description: '点这里可以全屏显示，但是请将你的浏览器升级到最新版本',
      position: 'left'
    }
  },
  {
    element: '#size-select',
    popover: {
      title: '调节字体大小',
      description: '为你贴心设计了可变的字体大小，可以根据你的需要修改字体大小',
      position: 'left'
    }
  },
  {
    element: '#tags-view-container',
    popover: {
      title: '快速标签栏',
      description: '你打开过得页面可以在这里找到，无需重新加载，快速切换',
      position: 'bottom'
    },
    padding: 0
  }
]

export default steps
