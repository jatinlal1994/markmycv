<template>
  <div class="page">
    <div id="top-section" class="clear">
      <div class="left">
        <p id="name">{{ name || "Full Name" }}</p>
        <p id="position">{{ position || "Position will be displayed here" }}</p>
      </div>
      <div class="right">
        <div class="info"><p><span><i class="fas fa-map-marker-alt"></i> <b>Location</b></span> {{ location || "State, Country name" }}</p></div>
        <div class="info"><p><span><i class="fas fa-envelope"></i> <b>Email ID</b></span> {{ emailid || "email@address.com" }}</p></div>
        <div class="info"><p><span><i class="fas fa-phone"></i> <b>Phone</b></span> {{ phone || "+1 9999 999999" }}</p></div>
      </div>
    </div>
    <div class="divider"></div>
    <div id="details-section" class="clear">
      <div id="social-links">
        <ul>
          <li v-if="github"><p><i class="fab fa-github-square"></i><span>Github URL : </span> {{ github }}</p></li>
          <li v-if="twitter"><p><i class="fab fa-twitter-square"></i><span>Twitter URL : </span> {{ twitter }}</p></li>
          <li v-if="linkedin"><p><i class="fab fa-linkedin"></i><span>Linkedin URL : </span> {{ linkedin }}</p></li>
          <li v-if="facebook"><p><i class="fab fa-facebook-square"></i><span>Facebook URL : </span> {{ facebook }}</p></li>
          <li v-if="reddit"><p><i class="fab fa-reddit-square"></i><span>Reddit URL : </span> {{ reddit }}</p></li>
          <li v-if="behance"><p><i class="fab fa-behance-square"></i><span>Behance URL : </span> {{ behance }}</p></li>
          <li v-if="youtube"><p><i class="fab fa-youtube"></i><span>YouTube URL : </span> {{ youtube }}</p></li>
        </ul>
      </div>
      <div id="details-box"><p><i class="fas fa-quote-left"></i> {{ summary || "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur mattis, magna nec finibus mollis, tellus ante fermentum dui, eget varius diam risus sit amet sapien." }} <i class="fas fa-quote-right"></i></p></div>
    </div>
    <div id="skills-section">
      <div class="section-title"><p>Technical skills</p></div>
      <ul>
      <li v-for="(skill, count) in skills" :key="count">
        <div class="skill-title"><p>{{ skill.type || "Title of skill" }}</p></div>
        <div class="skill-content"><p>{{ skill.description || "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris vehicula massa sed viverra auctor. Sed sed interdum tortor. Curabitur pulvinar augue." }}</p></div>
      </li>
      </ul>
    </div>
    <div class="divider not-first"></div>
    <div id="languages-section" class="clear">
    <div id="profile-pic" :style="profilepicture"></div>
      <div id="professional">
        <div class="section-title"><p>Career Objective</p></div>
        <div class="professional-string"><p>{{ objective || "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam porttitor convallis vestibulum. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Suspendisse et augue nec odio scelerisque fringilla vel ac justo. Sed a posuere risus, at dignissim odio. Sed tempus turpis a tortor sodales tempor." }}</p></div>
        <div class="professional-sub-title"><p>Core Skills</p></div>
        <div class="professional-sub-content"><p>{{ core_skills || "Lorem ipsum  - Dolor sit amet - Consectetur Adipiscing - Aliquam Porttitor - Convallis Vestibulum - Morbi Tristique - Senectus Netus - Malesuada Fames" }}</p></div>
        <div class="skill-images">
          <div class="clear">
            <div class="skill-col" v-for="(skill, count) in skillscore" :key="count">
              <div class="skill">
                <p class="skill-name">{{ skill.name || "Skill " + (count+1) + " Name" }} <span><b v-if="skillpercent">{{ skill.score || "50" }}%</b></span></p>
                <div class="skill-bar"><div class="skill-fill" :style="skill.style"></div></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="divider not-first"></div>
    <div id="career-section" class="clear">
      <div class="section-title">
        <p>Career Timeline</p>
      </div>
      <div class="career-step" v-for="(step, count) in timeline" :key="count">
        <p class="career-title">{{ step.position || "Position in Company" }} - {{ step.organisation_name || "Company Name" }} <span><b>( {{ step.from || "Month, Year" }} - {{ step.to || "Month, Year" }} )</b></span></p>
        <ul><li v-for="(achievement, subcount) in step.achievements" :key="subcount">{{ achievement.data || "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris vehicula massa sed viverra auctor. Sed sed interdum tortor. Curabitur pulvinar augue." }}</li></ul>
      </div>
    </div>
    <div class="divider not-first"></div>
    <div id="education-section">
      <div class="section-title">
        <p>Education</p>
      </div>
      <div id="education-row" class="clear">
        <div class="education-col" v-for="(education, count) in educations" :key="count">
          <p class="course-name"><b>{{ education.course_name || "Course name" }}</b></p>
          <p class="course-institute"><b>{{ education.institute || "Institution name" }}</b></p>
          <p class="course-year">{{ education.from || "Month, Year" }} - {{ education.to || "Month, Year" }}</p>
          <p class="course-marks">{{ education.score || "Marks or C.G.P.A." }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PrimaryResume',
  props: { hashcode: String, name: String, position: String, location: String, emailid: String, phone: String, profile: String, summary: String, skills: Array, timeline: Array, skillscore: Array, educations: Array, objective: String, core_skills: String, facebook: String, behance: String, linkedin: String, youtube: String, twitter: String, reddit: String, github: String, skillpercent: Boolean },
  methods: {
    width: function (pixels) {
      return 'width: ' + pixels
    }
  },
  computed: {
    profilepicture: function () {
      let hashcode = this.$data.hashcode
      if (hashcode === '') {
        return 'background-image: url("https://via.placeholder.com/166x263/53c043/f6f6f6.png?text=Profile")'
      } else {
        return 'background-image: url("http://localhost:8000/api/image/' + this.$props.hashcode + '")'
      }
    }
  }
}
</script>

<style lang="scss" scoped>
$theme: #87D37C;
body, p, a, ul, li{margin: 0;padding: 0;}
p, a, li{font-family: 'Poppins', sans-serif;color: #333;}
i, img{vertical-align: middle;}
li{list-style-type: none;}
.page{width: 793px;height: 1120px;margin: 0 auto;background-color: #fff;transform: scale(0.5) translate(0%, -50%);box-shadow: -2px 2px 5px 0 rgba(0,0,0,0.15);}
.left{float: left;}
.right{float: right;}
.clear:after{clear: both;display: block;content: "";}
.divider{height: 4px;width: calc(100% - 20px);margin: 0 auto;background-color: $theme;
  &.not-first{margin-top: 10px;margin-bottom: 10px;}
}
.section-title{margin-bottom: 8px;font-weight: 500;}
  #top-section{border-top: 5px solid $theme;padding: 0 10px;
  #name{font-size: 32px;font-weight: 400;margin-bottom: -4px;color: $theme;}
  #position{font-size: 12px;margin-left: 3px;margin-bottom: 10px;font-weight: 500;}
  .info{text-align: left;border-left: 2px solid #333;padding-left: 7px;
    p{font-size: 11.4px;line-height: 19px;font-weight: 500;color: #555;
      span{font-weight: 500;display: inline-block;width: 78px;
        i{width: 16px;text-align: center;}
      }
    }
  }
  .right{padding: 7px 0;}
}
#details-section{padding: 0 15px;
  #social-links{float: left;padding: 10px 0;
    p{font-size: 11.4px;font-weight: 400;line-height: 18px;
      i{margin-right: 4px;font-size: 1.1em;}
      span{font-weight: bold;display: inline-block;}
      &.social-github{}
      &.social-linkedin{}
      &.social-facebook{}
    }
  }
  #details-box{width: 52%;padding: 12px 0;float: right;
    p{font-size: 11px;color: #555;font-weight: 400;font-weight: bold;word-break: break-word;
      i{font-size: 7px;vertical-align: super;
        &:first-child{margin-right: 2px;}
        &:last-child{margin-left: 2px;}
      }
    }
  }
}
#skills-section{padding: 0 15px;font-size: 15px;font-weight: 500;
  ul{
    li{margin-bottom: 3px;border-bottom: 1px solid #eee;padding-bottom: 2px;
      &:after{clear: both;display: block;content: "";}
      &:last-child{border-bottom: none;}
    }
    .skill-title{width: 160px;float: left;
      p{font-weight: 500;}
    }
    .skill-content{width: calc(100% - 160px);float: left;
      p{font-weight: 400;}
    }
    p{font-size: 11px;
      span{display: inline-block;width: 30%;}
    }
  }
}
#languages-section{padding: 0 15px;font-size: 15px;font-weight: 500;
  .skill{margin-bottom: 12px;}
  #profile-pic{width: 166px;float: left;min-height: 1px;background: url('/profile.jpg');background-size: cover;height: 263px;;background-position: center center;}
  #professional{width: calc(100% - 180px);float: left;padding-left: 15px;box-sizing: border-box;
    .professional-string{
      p{font-size: 11.4px;font-weight: 400;}
    }
  }
  .professional-sub-title{margin-top: 5px;
    p{font-size: 12.8px;font-weight: 500;}
  }
  .professional-sub-content{margin-top: 3px;
    p{font-size: 11.4px;font-weight: 400;}
  }
  .skill-images{margin-top: 20px;
    .skill-col{width: 33.33%;float: left;padding: 0 10px;box-sizing: border-box;
      .skill-name{font-size: 11px;font-weight: bold;margin-bottom: 3px;margin-left: 4px;padding-right: 6px;
        span{color: darken($theme, 15%);font-size: 0.9em;font-weight: 500;float: right;}
      }
      .skill-bar{width: 100%;height: 5px;background-color: #ddd;border-radius: 4px;overflow: hidden;margin-bottom: 8px;
        .skill-fill{background-color: $theme;height: 100%;
          &#english{width: 80%;}
          &#html{width: 85%;}
          &#scss{width: 75%;}
          &#python{width: 80%;}
          &#django{width: 85%;}
          &#docker{width: 70%;}
        }
      }
    }
  }
}
#career-section{padding: 0 15px;font-size: 15px;font-weight: 500;
  .career-step{padding: 0 5px;
    span, a{font-weight: bold;}
  }
  .career-title{margin-bottom: 2px;font-size: 13px;
    span{font-size: 10px;color: darken($theme, 15%);font-weight: 500;}
  }
  a{text-decoration: none;color: darken($theme, 20%);}
  ul{margin-left: 20px;margin-bottom: 5px;
    li{font-size: 11.4px;list-style-type: square;font-weight: 400;color: #555;}
  }
}
#education-section{padding: 0 15px;font-size: 15px;font-weight: 500;
  .education-col{width: 33.33%;float: left;border-right: 3px solid $theme;box-sizing: border-box;padding: 0 15px;text-align: left;
    .course-name{font-size: 12px;color: darken($theme, 15%);font-weight: 500;}
    .course-institute{font-size: 11.4px;font-weight: 500;}
    .course-year{font-size: 11.4px;font-weight: 500;}
    .course-marks{font-size: 11.4px;}
    &:last-child{border-right: none;}
  }
}
@media print {
  .page{transform: scale(1) translate(0%, 0%);}
}
@media(min-width: 1200px) and (max-width: 1400px) {
  #editor-area{width: calc(100vw - 600px);}
  #preview-area{width: 600px;}
  //.page{transform: scale(0.5) translate(-25%, -50%);transform: scale(0.6) translate(-20%, -32%);}
}
@media(min-width: 1400px) {
  #editor-area{width: 50%;}
  #preview-area{width: 50%;}
  .page{transform: scale(0.5) translate(0%, -50%);transform: scale(0.6) translate(0%, -30%);}
}
</style>
