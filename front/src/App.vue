<template>
  <div class="content">
    <div v-if="showPopupNo !== 3" class="logo">
      <img src="@/assets/logo.png" />
    </div>
    <Map
        :map="map"
        :map-active="mapActive"
        :messages="messages"
        :tile-chosen="tileChosen"
        :object-chosen="objectVariationChosen"
        @choose-tile="chooseTile"
    />
    <Popup
        :api-url="apiUrl"
        :tile-chosen-id="tileChosen"
        :object-variation-chosen="objectVariationChosen"
        :show-popup-no="showPopupNo"
        :token="token"
        @object-chosen="objectIsChosen"
        @variation-chosen="variationIsChosen"
        @thank-you="thankYou"
        @back-to-object="backToObject"
        @back-to-variation="backToVariation"
        @new-message="addMessage"
    />
    <SignaturesPopup v-if="showPopupNo !== 3" />
  </div>

</template>

<script>
import Map from './components/Map.vue'
import Popup from './components/Popup.vue'
import SignaturesPopup from "./components/SignaturesPopup";

export default {
  name: 'App',
  components: {
    SignaturesPopup,
    Map,
    Popup
  },
  data() {
    return {
      apiUrl: "https://stanovanjske-zadruge-zemljevid.lb.djnd.si",
      // apiUrl: 'http://0.0.0.0:8000',
      map: [],
      messages: {},
      tileChosen: null,
      objectVariationChosen: null,
      mapActive: false,
      token: '',
      tokenConfirmed: false,
      showPopupNo: 5
    }
  },
  async created() {
    await this.axios.get(this.apiUrl + '/api/map/').then((res) => {
      if (res.status === 200) {
        this.map = res.data.data.map
      } else {
        console.log('error')
      }
    })
    await this.axios.get(this.apiUrl + '/api/message/').then((res) => {
      if (res.status === 200) {
        const messages = {}
        for (const message of res.data.data) {
          messages[message.index] = message.text;
        }
        this.messages = messages
      } else {
        console.log('error')
      }
    })
    this.token = this.$route.query.token
    if (this.token) {
      await this.axios.get(this.apiUrl + '/api/token/?token=' + this.token).then((res) => {
        if (res.status === 200) {
          console.log(res)
          if (res.data.status === "success") {
            this.tokenConfirmed = true
            this.showPopupNo = 1
          }
        }
      }).catch((err) => {
        console.log(err);
      })
    }
  },
  methods: {
    async placeOnMap(i) {
      console.log('a to se dogaja')
      this.objectChosen = i
      if (this.tileChosen && this.objectChosen) {
        this.map[this.tileChosen] = this.objectChosen
        console.log({
          'map': this.map,
          'token': this.token
        })
        await this.axios.post(this.apiUrl + '/api/map/', {
          'map': this.map,
          'token': this.token
        }).then((res) => {
          if (res.status === 200) {
            document.getElementById('tile-' + this.tileChosen).style.backgroundImage = "url(" + require('@/assets/tiles/' + this.objectChosen + '.png') + ")";
            console.log('success');
          } else {
            alert("Nekaj je šlo narobe :(")
            console.log('error')
          }
        }).catch((err) => {
          console.log(err)
        })
      }
    },
    addMessage(message) {
      this.messages[message.index] = message.text;
    },
    objectIsChosen() {
      this.showPopupNo++
    },
    thankYou() {
      this.showPopupNo++
    },
    backToObject() {
      this.objectChosen = null
      this.showPopupNo--
    },
    backToVariation() {
      this.objectVariationChosen = null
      this.showPopupNo--
    },
    variationIsChosen(n) {
      this.objectVariationChosen = n
      this.mapActive = true
      this.showPopupNo++
    },
    async chooseTile(i) {
      this.tileChosen = i

      if (this.tileChosen && this.objectVariationChosen) {
        this.map[this.tileChosen] = this.objectVariationChosen
        await this.axios.post(this.apiUrl + '/api/map/', {
          "map": this.map,
          'token': this.token
        }).then((res) => {
          if (res.status === 200) {
            document.getElementById('tile-' + this.tileChosen).style.backgroundImage = "url(" + require('@/assets/tiles/' + this.objectVariationChosen + '.png') + ")";
            console.log('success');
            this.mapActive = false
            this.showPopupNo++
          } else {
            alert("Nekaj je šlo narobe :(")
            console.log('error')
          }
        })
      }
    },
  }
}
</script>

<style>
html, body {
  margin: 0;
  padding: 0;
}
#app {
}
.content {
  position: relative;
  overflow: scroll;
}
.logo {
  position: fixed;
  z-index: 1000;
  left: 40px;
  top: 30px;
  pointer-events: none;
}
.logo img {
  width: 90px;
  height: 90px;
}
@media (min-width: 992px) {
  .logo {
    display: block;
  }
  .logo img {
    width: 120px;
    height: 120px;
  }
  .content {
    position: relative;
    overflow: unset;
  }
}
</style>
