<template>
  <div id="about-page">
    <div id="back-section">
      <div class="left">
        <router-link to="/">
          <p>
            <span>
              <i class="fas fa-chevron-left"></i> Back to home
            </span>
            </p>
        </router-link>
      </div>
    </div>
    <div id="top-section">
        <div id="top-section-row">
          <div class="top-section-col">
            <div class="welcome-vertical">
              <p class="hello">Hello, I'm</p>
              <p class="dev-name">Jatin Lal</p>
              <p class="position">Full Stack Web Developer and UI Designer</p>
              <p class="mode-about-me">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas sollicitudin enim nisi, at viverra augue egestas et. </p>
              <div class="contact-button">
                <a href="#"><i class="fas fa-envelope"></i>Contact by mail</a>
              </div>
            </div>
          </div>
          <div class="top-section-col">
            <div class="main-content">
              <div class="main-content-vertical">
                <div class="connect-me">
                  <p>Connect with me</p>
                </div>
                <div class="connect-me-desc">
                  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. <br> Sollicitudin condimentum enim eget.</p>
                </div>
                <div id="social-icons">
                  <div class="social-icons-row">
                    <div class="social-icon">
                      <a href="#">
                        <i class="fab fa-facebook-square"></i>
                      </a>
                    </div>
                    <div class="social-icon">
                      <a href="#">
                        <i class="fab fa-twitter-square"></i>
                      </a>
                    </div>
                    <div class="social-icon">
                      <a href="#">
                        <i class="fab fa-linkedin"></i>
                      </a>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    <div id="about-page-container">
      <div class="globe-section">
        <img src="../images/about/world.svg">
      </div>
      <div class="about-inner">
        <div class="about-description-row">
          <div class="title">
            <p>Overview</p>
          </div>
          <div class="description">
            <p>Mark My CV is a great tool for building an attractive Resume. We've made it surprisingly easy for you to create your Resume. Our goal is to provide the best and easiest resume building experience on the Internet, and establish MarkMyCV.com as the most effective online destination for Resume creation.</p>
          </div>
        </div>
        <div class="about-description-row">
          <div class="title">
            <p>Description</p>
          </div>
          <div class="description">
            <p>Use MarkMyCV to quickly create descriptive, attractive and beautiful Resume for your future job. All our Templates are refined multiple times to match the needs of recruiters. The Website also offers </p>
          </div>
        </div>
      </div>
      <div id="footer-section">
        <p><i class="far fa-copyright"></i> MarkMyCV | All Rights Reserved</p>
      </div>
    </div>
  </div>
</template>

<style lang="scss">
#about-page{background-color: #fff;
  #back-section{background-color: #fff;padding-bottom: 15px;
    p{background-color: #16A085;color: #fff;line-height: 38px;width: 38px;text-align: center;border-radius: 0 0 5px 0;font-size: 18px;cursor: pointer;display: table-row-group;font-size: 12px;font-weight: 600;border-radius: 0 0 5px 0;overflow: hidden;span{padding: 0 12px;}i{margin-right: 5px;}}
  }
  #about-page-container{width: 1080px;margin: 0 auto;}
  #top-section{
    #top-section-row{height: 360px;width: 100%;overflow: hidden;background: #fff;
      .top-section-col{width: 50%;float: left;height: 100%;display: table;padding: 0px 8%;box-sizing: border-box;
        &:first-child{}
        &:last-child{position: relative;text-align: center;
          .main-content{position: absolute;width: 100%;left: 100%;top: 0;left: 0;z-index: 3;display: table;height: 100%;
            .main-content-vertical{display: table-cell;vertical-align: middle;padding: 0 14%;
              .connect-me{font-size: 22px;font-weight: 500;color: lighten(#16A085, 58%);margin-bottom: 4px;}
              .connect-me-desc{color: lighten(#16A085, 58%);font-size: 12px;font-weight: 500;}
            }
          }
          &:after{display: block;content: "";background-color: #16A085;position: absolute;width: 110%;height: 100%;top: 0;left: 0;transform: skew(14deg, 0deg);border-radius: 10px 0 0 10px;}
        }
      }
      &:after{clear: both;display: block;content: "";}
    }
    .welcome-vertical{display: table-cell;vertical-align: middle;
      .hello{font-size: 22px;font-weight: 500;color: #34495E;margin-left: 4px;}
      .dev-name{color: #16A085;font-size: 38px;font-weight: bold;margin-bottom: 6px;}
      .position{font-size: 13px;font-weight: 500;margin-left: 4px;margin-bottom: 4px;color: #34495E;}
      .mode-about-me{font-size: 11px;font-weight: 500;margin-left: 4px;color: #7F8C8D;}
    }
  }
  #social-icons{padding: 0 10px;padding-top: 10px;
    .social-icons-row{margin: 0 -8px;
      &:after{clear: both;display: block;content: "";}
    }
    .social-icon{display: inline-block;padding: 0 8px;
      i{font-size: 20px;color: lighten(#16A085, 58%);
      }
    }
  }
  #about-us-text{background-color: #fff;padding: 20px 25px 25px 30px;
    p{font-size: 12px;margin-bottom: 8px;font-weight: 500;color: #7F8C8D;}
  }
  .contact-button{margin: 12px 0 0 4px;
    a{border-radius: 4px;background-color: #16A085;padding: 5px 10px;color: lighten(#16A085, 58%);font-size: 11px;font-weight: 600;
      i{margin-right: 6px;font-size: 1.1em;vertical-align: middle}
    }
  }
  .globe-section{background-color: #fff;padding: 45px 0 15px 0;
    img{width: 180px;margin: 0 auto;display: block;animation: jump 2.5s infinite;}
  }
  .about-inner{padding: 0 15px;background-color: #fff;padding-top: 18px;}
  .about-description-row{padding: 10px 15px;border-bottom: 1px solid #ECF0F1;
    .title{width: 180px;float: left;padding: 5px 15px;box-sizing: border-box;font-size: 13px;color: #16A085;font-weight: 600;}
    .description{width: calc(100% - 180px);float: left;padding: 5px 15px;box-sizing: border-box;font-size: 12px;color: #7F8C8D;border-left: 1px solid #ECF0F1;}
    &:last-child{border-bottom: 0;}
    &:after{clear: both;display: block;content: "";}
  }
  @keyframes jump {
    0% {transform: translateY(-5px);}
    50% {transform: translateY(5px);}
    100% {transform: translateY(-5px);}
  }
  #footer-section{background-color: #fff;padding: 20px 15px;text-align: center;font-size: 12px;font-family: 'Poppins';font-weight: 500;color: #BDC3C7;
    i{font-size: 0.9em;}
  }
}
</style>
