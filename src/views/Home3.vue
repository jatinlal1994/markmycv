<template>
  <div id="home-content">
    <div :class="navClass" id="home-nav">
      <Nav @login="login_username" @closeHome="closeHome" ref="nav" />
    </div>
    <div id="home-banner">
      <div id="home-banner-vertical">
        <div class="home-banner-inner">
          <div class="home-banner-container">
            <div class="home-banner-box">
              <div class="home-banner-text">
                <p :class="textClass">MARK</p>
              </div>
              <div id="home-banner-square" :class="squareClass"></div>
              <div class="home-banner-text">
                <p :class="textClass">MYCV</p>
              </div>
            </div>
          </div>
        </div>
        <div class="welcome-text">
          <p>Welcome to MarkMyCV</p>
        </div>
        <div class="welcome-message">
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
        </div>
      </div>
    </div>
    <div id="home-features"></div>
  </div>
</template>

<style lang="scss">
#home-content{
  #home-nav{height: 48px;background-color: #fff;box-shadow: 0 0px 4px 0 rgba(0,0,0,0.12);position: fixed;top: 0;left: 0;z-index: 2;
    .left{float: left;}
    .right{float: right;}
  }
  #home-banner{height: 625px;width: 100vw;display: table;background-color: #fff;
    #home-banner-vertical{display: table-cell;vertical-align: middle;
      .home-banner-container{width: 120px;margin: 0 auto;
        #home-banner-square{height: 180px;width: 100%;border: 3px solid #555;box-sizing: border-box;border-radius: 0px;opacity: 1;transition: 1000ms;
          &.sliding{opacity: 0;}
          &:before{display: block;content: "";position: absolute;top: 25px;height: 67px;width: 3px;background: #fff;left: 0.3px;z-index: 1;}
        }
        .home-banner-box{position: relative;}
        .home-banner-text{background: #fff;z-index: 4;
          p{font-size: 36px;font-weight: 600;color: #555;font-weight: 100;transform: translate(0px);opacity: 1;transition: 1000ms;
            &.sliding{opacity: 0;}
          }
          &:first-child{top: 14%;left: -48px;
            p.sliding{transform: translate(-50px);}
          }
          &:last-child{bottom: 14%;right: -48px;
            p.sliding{transform: translate(50px);}
          }
          &:first-child, &:last-child{position: absolute;padding: 6px 0;background: #fff;}
        }
      }
    }
    .welcome-text{text-align: center;margin-top: 38px;font-size: 20px;
      p{font-weight: 500;color: #555;}
    }
    .welcome-message{text-align: center;width: 40%;margin: 0 auto;margin-top: 25px;font-size: 14px;
      p{line-height: 24px;font-weight: 500;color: #666;}
    }
  }
  #home-features{height: 600px;width: 100%;background: #f6f6f6;}
}
</style>

<script>
import Nav from '@/components/Nav'

export default {
  name: 'Home',
  data () {
    return {
      squareClass: 'sliding',
      textClass: 'sliding',
      navClass: ''
    }
  },
  mounted () {
    let data = this.$data
    setTimeout(function () {
      data.squareClass = ''
      setTimeout(function () {
        data.textClass = ''
      }, 750)
    }, 250)
  },
  methods: {
    handleScroll (event) {
      let data = this.$data
      if (document.documentElement.scrollTop > 0) {
        data.navClass = 'solid'
      } else {
        data.navClass = ''
      }
    }
  },
  components: {
    Nav
  },
  created () {
    window.addEventListener('scroll', this.handleScroll)
  },
  destroyed () {
    window.removeEventListener('scroll', this.handleScroll)
  }
}
</script>
