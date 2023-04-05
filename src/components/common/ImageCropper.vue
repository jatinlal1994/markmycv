<template>
    <div>
        <vue-croppie ref="croppieRef" :enableOrientation="true" :boundary="{ width: 80, height: 80}" @result="result" @update="update"></vue-croppie>
        <img v-bind:src="cropped">
        <button @click="bind()">Bind</button>
        <button @click="rotate(-90)">Rotate Left</button>
        <button @click="rotate(90)">Rotate Right</button>
        <button @click="crop()">Crop Via Callback</button>
        <button @click="cropViaEvent()">Crop Via Event</button>
    </div>
</template>

<script>
import 'vue-croppie'
export default {
  name: 'ImageCropper',
  mounted () {
    this.$refs.croppieRef.bind({
      url: 'http://i.imgur.com/Fq2DMeH.jpg'
    })
  },
  data () {
    return {
      cropped: null,
      images: [
        'http://i.imgur.com/fHNtPXX.jpg',
        'http://i.imgur.com/ecMUngU.jpg',
        'http://i.imgur.com/7oO6zrh.jpg',
        'http://i.imgur.com/miVkBH2.jpg'
      ]
    }
  },
  methods: {
    bind () {
      let url = this.images[Math.floor(Math.random() * 4)]
      this.$refs.croppieRef.bind({
        url: url
      })
    },
    crop () {
      let options = {
        format: 'jpeg',
        circle: true
      }
      this.$refs.croppieRef.result(options, (output) => {
        this.cropped = output
      })
    },
    cropViaEvent () {
      let options = {
        format: 'jpeg',
        circle: true
      }
      this.$refs.croppieRef.result(options)
    },
    result (output) {
      this.cropped = output
    },
    update (val) {
      console.log(val)
    },
    rotate (rotationAngle) {
      this.$refs.croppieRef.rotate(rotationAngle)
    }
  }
}
</script>
