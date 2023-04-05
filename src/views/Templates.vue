<template>
  <div id="templates-content">
    <Nav @login="login_username" @closeHome="closeHome" />
    <div id="templates-background" :class="background_status"></div>
    <div id="background-overlay" :class="overlay_class"></div>
    <div id="templates-content-inner">
      <div id="templates-title">
        <p class="title">Pick a Template</p>
        <p class="sub-title">Select a Template from list given below</p>
      </div>
      <div id="templates-list">
        <div id="templates-list-inner">
          <div class="template">
            <router-link to="/template/primary">
              <div class="template-inner">
                <div class="image">
                  <img width="205" height="289" alt="Primary Template" src="../images/templates/primary-resume.png">
                </div>
                <div class="text">
                  <p>Primary Theme</p>
                </div>
                <div class="desc">
                  <p>Basic template to start from</p>
                </div>
              </div>
            </router-link>
          </div>
          <div class="template">
            <router-link to="/template/primary">
              <div class="template-inner">
                <div class="image">
                  <img width="205" height="289" alt="Primary Template" src="../images/templates/primary-resume.png">
                </div>
                <div class="text">
                  <p>Primary Theme</p>
                </div>
                <div class="desc">
                  <p>Basic template to start from</p>
                </div>
              </div>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Nav from '@/components/Nav'

export default {
  name: 'templates',
  metaInfo: {
    title: 'Access our attractive and easy to use Templates for your CV',
    titleTemplate: 'MarkMyCV - %s',
    htmlAttrs: {
      lang: 'en',
      amp: true
    }
  },
  components: {
    Nav
  },
  data () {
    return {
      background_status: '', overlay_class: '', login_username: '', is_logged_in: false, main_string: 'Stunning', main_string_class: '', to_width: 0
    }
  },
  methods: {
    closeHome (value) {
      let data = this.$data
      data.background_status = value
      if (value === 'opened') {
        data.overlay_class = 'opening'
        setTimeout(function () {
          data.overlay_class = 'opened'
        }, 10)
      } else {
        data.overlay_class = 'opening'
        setTimeout(function () {
          data.overlay_class = ''
        }, 500)
      }
    }
  }
}
</script>

<style lang="scss" scoped>
#templates-background{position: fixed;top: 0;left: 0;width: 100vw;height: 100vh;z-index: -1;background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('../images/home-bk.jpg');background-size: cover;background-position: center;transform: scale(1.1);filter: blur(2px);transition: 500ms left;
  &.opened{transform: scale(1.1);left: 20px;}
}
#templates-title{
  p{
    &.title{font-size: 24px;font-weight: 600;text-align: center;color: #f6f6f6;}
    &.sub-title{font-size: 12px;font-weight: 600;text-align: center;color: #f6f6f6;margin-top: 4px;}
  }
}
#templates-sub-title{
  p{font-size: 24px;font-weight: 600;text-align: center;color: #f6f6f6;}
}
#templates-list{position: fixed;top: 190px;width: 88%;height: calc(100vh - 210px);
  #templates-list-inner{height: 500px;padding-top: 15px;
    .template{width: 20%;float: left;padding: 0 15px;box-sizing: border-box;
      .template-inner{background-color: rgba(255,255,255,0.1);border-radius: 4px;margin-bottom: 30px;transition: 250ms;}
      .image{padding: 20px 15px 5px 15px;
        img{width: 100%;vertical-align: middle;box-shadow: 0px 2px 6px 0 rgba(0, 0, 0, 0.2);}
      }
      .text{padding: 3px 10px 0px 10px;
        p{font-size: 15px;font-weight: 600;color: #F6F6F6;text-shadow: -2px 2px 5px rgba(0,0,0,0.15);}
      }
      .desc{padding: 3px 10px 15px 10px;
        p{font-size: 11px;font-weight: 400;color: #ECF0F1;font-weight: 600;text-shadow: -2px 2px 5px rgba(0,0,0,0.15);}
      }
      .text, .desc{text-align: center;}
      .template-inner{
        &:hover{background-color: rgba(240, 240, 240, 1);
          p{color: #333;}
        }
      }
    }
  }
}
#templates-content-inner{padding: 7.5% 6% 0% 6%;}
</style>
