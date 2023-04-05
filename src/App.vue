<template>
  <div id="root">
    <router-view />
  </div>
</template>

<style lang="scss">
@font-face{font-family: 'Barcelony';src: url('./fonts/barcelony.ttf') format('truetype');}
*{-webkit-font-smoothing: antialiased;-moz-osx-font-smoothing: grayscale;}
body{background-color: #f6f6f6;}
body, div, p, a, ul, li, input, button, textarea{margin: 0;padding: 0;}
div, p, a, ul, li, button{font-family: 'Poppins', sans-serif;}
input, textarea{font-family: 'Barlow', sans-serif;}
a{text-decoration: none;}
a, input, textarea, button{
  &, &:hover, &:focus, &:active{border: none;outline: none;}
}
li{list-style-type: none;}
.modal{position: fixed;top: 0;left: 0;width: 100vw;height: 100vh;background-color: rgba(0,0,0,0.5);transition: 500ms opacity;z-index:5;
  .modal-vertical{display: table-cell;vertical-align: middle;
    .modal-container{width: 100%;max-width: 540px;padding: 0 15px;box-sizing: border-box;margin: 0 auto;
      .modal-box{min-height: 100px;background-color: #fff;border-radius: 5px;transition: 500ms;position: relative;padding-bottom: 10px;padding-top: 40px;
        .modal-title{line-height: 40px;font-weight: 600;font-size: 13px;padding: 0 12px;position: absolute;top: 0;left: 0;width: 100%;box-sizing: border-box;}
        .close-modal{position: absolute;top: 8px;right: 15px;cursor: pointer;z-index: 5;
          i{font-size: 18px;}
        }
      }
    }
  }
  &.closed{display: none;opacity: 0;background-color: rgba(0,0,0,0.0);
    .modal-box{transform: translateY(-4vh);}
  }
  &.opening{display: table;opacity: 0;background-color: rgba(0,0,0,0.0);
    .modal-box{transform: translateY(-4vh);}
  }
  &.opened{display: table;opacity: 1;background-color: rgba(0,0,0,0.5);
    .modal-box{transform: translateY(0vh);}
  }
}
@keyframes shake {
  0% { transform: translateX(2px) }
  25% { transform: translateX(-2px) }
  50% { transform: translateX(2px) }
  75% { transform: translateX(-2px) }
  100% { transform: translateX(2px) }
}
</style>
