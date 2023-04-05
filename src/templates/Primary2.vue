<template>
  <div>
    <div id="inner-nav"></div>
    <div id="templates-page-row">
      <div id="templates-editor">
        <div id="editor-title"><p>Basic Information</p></div>
        <div class="fields-hint">
          <div class="fields-hint-inner">
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur et ligula vel lacus tristique condimentum. Duis dictum risus eu est vestibulum, vel malesuada mauris bibendum. Proin ac iaculis massa, eu volutpat nisl.</p>
            <ul>
              <li>Sed dapibus sodales magna in interdum. Phasellus scelerisque ornare feugiat. </li>
              <li>Etiam vitae pulvinar dolor, commodo semper velit. Donec non massa sapien. Proin maximus consequat tellus et interdum.</li>
            </ul>
          </div>
        </div>
        <div id="basic-info" class="editor-section">
          <div class="field">
            <label>Full Name</label>
            <input type="text" placeholder="Enter Full Name" />
          </div>
          <div class="field">
            <label>Position</label>
            <input type="text" placeholder="Enter Position" />
          </div>
        </div>
        <div id="editor-title"><p>Contact Information</p></div>
        <div class="fields-hint">
          <div class="fields-hint-inner">
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur et ligula vel lacus tristique condimentum. Duis dictum risus eu est vestibulum, vel malesuada mauris bibendum. Proin ac iaculis massa, eu volutpat nisl.</p>
            <ul>
              <li>Sed dapibus sodales magna in interdum. Phasellus scelerisque ornare feugiat. </li>
              <li>Etiam vitae pulvinar dolor, commodo semper velit. Donec non massa sapien. Proin maximus consequat tellus et interdum.</li>
            </ul>
          </div>
        </div>
        <div id="contact-info" class="editor-section">
          <div class="field">
            <label>Location</label>
            <input type="text" placeholder="Enter Location" />
          </div>
          <div class="field">
            <label>Email ID</label>
            <input type="text" placeholder="Enter Email ID" />
          </div>
          <div class="field">
            <label>Contact No.</label>
            <input type="text" placeholder="Enter Contact No." />
          </div>
        </div>
        <div id="editor-title"><p>Basic Information</p></div>
        <div class="fields-hint">
          <div class="fields-hint-inner">
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur et ligula vel lacus tristique condimentum. Duis dictum risus eu est vestibulum, vel malesuada mauris bibendum. Proin ac iaculis massa, eu volutpat nisl.</p>
            <ul>
              <li>Sed dapibus sodales magna in interdum. Phasellus scelerisque ornare feugiat. </li>
              <li>Etiam vitae pulvinar dolor, commodo semper velit. Donec non massa sapien. Proin maximus consequat tellus et interdum.</li>
            </ul>
          </div>
        </div>
        <div class="fields-section-content">
          <div class="special-field-wrapper field">
          <div class="special-field-card">
            <div class="special-icon social-icon">
              <i class="fab fa-github-square"></i>
            </div>
            <div class="special-field">
              <label> Github Profile</label>
              <input placeholder="Enter Github URL" type="text" v-model="github" />
            </div>
          </div>
          </div>
          <div class="special-field-wrapper field">
          <div class="special-field-card">
            <div class="special-icon social-icon">
              <i class="fab fa-facebook-square"></i>
            </div>
            <div class="special-field">
              <label> Facebook Profile</label>
              <input placeholder="Enter Facebook URL" type="text" v-model="facebook" />
            </div>
          </div>
          </div>
          <div class="special-field-wrapper field">
          <div class="special-field-card">
            <div class="special-icon social-icon">
                <i class="fab fa-reddit-square"></i>
            </div>
            <div class="special-field">
                <label> Reddit Profile</label>
                <input placeholder="Enter Reddit URL" type="text" v-model="reddit" />
            </div>
          </div>
          </div>
          <div class="special-field-wrapper field">
          <div class="special-field-card">
            <div class="special-icon social-icon">
                <i class="fab fa-twitter-square"></i>
            </div>
            <div class="special-field">
                <label> Twitter Profile</label>
                <input placeholder="Enter Twitter URL" type="text" v-model="twitter" />
            </div>
          </div>
          </div>
          <div class="special-field-wrapper field">
          <div class="special-field-card">
            <div class="special-icon social-icon">
                <i class="fab fa-linkedin"></i>
            </div>
            <div class="special-field">
                <label> Linkedin Profile</label>
                <input placeholder="Enter Linkedin URL" type="text" v-model="linkedin" />
            </div>
          </div>
          </div>
          <div class="special-field-wrapper field">
          <div class="special-field-card">
            <div class="special-icon social-icon">
                <i class="fab fa-behance-square"></i>
            </div>
            <div class="special-field">
                <label> Behance Profile</label>
                <input placeholder="Enter Behance URL" type="text" v-model="behance" />
            </div>
          </div>
          </div>
          <div class="special-field-wrapper field">
          <div class="special-field-card">
            <div class="special-icon social-icon">
                <i class="fab fa-youtube"></i>
            </div>
            <div class="special-field">
                <label> YouTube Channel</label>
                <input placeholder="Enter YouTube URL" type="text" v-model="youtube" />
            </div>
          </div>
          </div>
      </div>
      </div>
      <div id="templates-preview"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Primary'
}
</script>

<style lang="scss">
  #inner-nav{height: 42px;background-color: #9B59B6;}
  #templates-page-row:After{clear: both;display: block;content: "";}
  #templates-editor{padding: 15px;left: 0;background-color: #f6f6f6;box-sizing: border-box;
    #editor-title{
      p{font-size: 16px;font-weight: 600;}
    }
    .field{float: left;padding: 0 10px;box-sizing: border-box;
      label{font-size: 11px;font-weight: 600;display: block;margin-bottom: 2px;margin-left: 2px;}
      input{height: 32px;width: 100%;border-radius: 4px;cursor: pointer;
        &:focus{background-color: #eee;
          &:hover{cursor: auto;}
        }
      }
    }
  }
  .fields-hint{padding: 10px 0px;
    .fields-hint-inner{background-color: #9B59B6;padding: 10px;font-size: 11px;font-weight: 600;color: #fff;border-radius: 5px;
      ul{margin-left: 25px;margin-top: 5px;
        li{list-style-type: disc;margin-bottom: 3px;}
      }
    }
  }
  input, textarea{font-size: 12px;padding: 0 8px;box-sizing: border-box;font-weight: 600;}
  .editor-section{padding: 0 5px 15px 5px;margin: 0 -10px 15px -10px;border-bottom: 1px solid #eee;
    &:after{clear: both;display: block;content: "";}
    &:last-child{border-bottom: 0;}
  }
  #basic-info{
    .field{width: 33.33%;}
  }
  #contact-info{
    .field{width: 33.33%;}
  }
  #templates-preview{left: 50%;background-color: #fff;}
  #templates-preview, #templates-editor{width: 50%;min-height: 1px;position: fixed;top: 42px;height: calc(100vh - 42px);overflow-y: auto;}
  .fields-section-content{
    label{color: #fff;}
    &.--textarea-section{padding: 0 10px;border-radius: 5px;margin-bottom: 15px;margin-top: 10px;
      .fields{background-color: rgba(0, 0, 0, 0.2);border-radius: 5px;box-shadow: -2px 2px 5px 0 rgba(0,0,0,0.15);padding: 5px;
      label{color: #fff;}
        textarea{border-radius: 5px 5px 5px 5px;border-bottom: 1px solid #eee;}
      }
    }
    &.--file-section{
      label{color: #fff;}
      .file-field{width: 100%;height: 100%;display: table;border: 3px dashed #ddd;box-sizing: border-box;}
      label{display: table !important;padding: 10px;box-sizing: border-box;color: #fff;cursor: pointer;transition: 120ms;
        .label-vertical{display: table-cell;vertical-align: middle;
          .label-container{text-align: center;color: #777;}
        }
        &:hover{background-color: #f6f6f6;}
      }
      input{display: none;}
      label{display: block;width: 30%;height: 160px;background-color: #eee;margin: 0 auto;
        &.true{background-color: #2ECC71;}
      }
    }
    .special-field-wrapper{width: 33.33%;float: left;box-sizing: border-box;}
    .section-sub-title{padding: 8px 10px 2px 10px;line-height: 16px;
      p{float: left;font-weight: bold;font-size: 13px;color: #fff;}
      .cancel-career-step{float: right;cursor: pointer;color: #fff;}
      &:after{clear: both;display: block;content: "";}
    }
    &:after{clear: both;display: block;content: "";}
  }
  .special-field-wrapper{width: 60%;padding: 8px;margin-bottom: 15px;
    .special-field-card{background-color: #fff;box-shadow: -2px 2px 5px 0 rgba(0,0,0,0.15);padding: 10px 8px 12px 8px;border-radius: 4px;
      .slider-box{margin-top: 74px;margin-bottom: 12px;padding: 0 10px;}
      .slider{-webkit-appearance: none;width: 100%;height: 6px;background: #d3d3d3;outline: none;opacity: 1;transition: opacity .2s;padding: 0;margin-top: 10px;border: none;box-shadow: inset 0px 0px 2px 0 rgba(0,0,0,0.2);
        &:hover {opacity: 1;}
        &::-webkit-slider-thumb{-webkit-appearance: none;appearance: none;width: 18px;height: 18px;background: #333;cursor: pointer;border-radius: 50%;border: 4px solid #2ECC71;background: #fff;box-shadow: -2px 2px 5px 0 rgba(0,0,0,0.15);}
        &::-moz-range-thumb{width: 25px;height: 25px;background: #333;cursor: pointer;border-radius: 50%;}
        &:after{clear: both;display: block;content: "";}
      }
      .special-icon.social-icon{background-color: #fff;border-radius: 4px;}
      &:after{clear: both;display: block;content: "";}
      .special-icon{float: left;margin-right: 8px;margin-left: 4px;width: 50px;text-align: center;
        i{font-size: 48px;line-height: 52px;color: #fff;
          &.fa-github-square{color: #333333;}
          &.fa-facebook-square{color: #3b5998;}
          &.fa-twitter-square{color: #1da1f2;}
          &.fa-linkedin{color: #0077b5;}
          &.fa-linkedin{color: #0077b5;}
          &.fa-reddit-square{color: #ff4500;}
          &.fa-behance-square{color: #1769ff;}
          &.fa-youtube{color: #ff0000;font-size: 42px;}
          &.fa-map-marker-alt{font-size: 40px;}
          &.fa-envelope{font-size: 40px;}
          &.fa-phone{font-size: 38px;}
          &.fa-crosshairs{font-size: 38px;}
          &.fa-user{font-size: 38px;}
        }
      }
      .special-field{float: left;width: calc(100% - 62px);
        label{margin: 0;color: #333;}
        input{width: 100%;}
      }
      &:after{clear: both;display: block;content: "";}
    }
  }
</style>
