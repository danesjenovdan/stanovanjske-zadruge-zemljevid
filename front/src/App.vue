<template>
  <div class="content">
    <div class="logo">
      <img src="@/assets/logo.png" />
    </div>
    <Map
        :map="map"
        :messages="messages"
        :tile-chosen="tileChosenId"
        :object-chosen="objectChosen"
        @choose-tile="chooseTile"
    />
    <Popup
        :api-url="apiUrl"
        :tile-chosen="tileChosen"
        :tile-chosen-id="tileChosenId"
        @place-on-map="placeOnMap"
        @new-message="addMessage"
    />
    <SignaturesPopup />
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
      map: [],
      messages: {},
      tileChosen: false,
      tileChosenId: null,
      objectChosen: null,
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
  },
  methods: {
    chooseTile(i) {
      this.tileChosen = true
      this.tileChosenId = i
    },
    async placeOnMap(i) {
      this.objectChosen = i
      if (this.tileChosen && this.objectChosen) {
        this.map[this.tileChosenId] = this.objectChosen
        await this.axios.post(this.apiUrl + '/api/map/', {
          "map": this.map
        }).then((res) => {
          if (res.status === 200) {
            document.getElementById('tile-' + this.tileChosenId).style.backgroundImage = "url(" + require('@/assets/tiles/' + this.objectChosen + '.png') + ")";
            console.log('success');
          } else {
            alert("Nekaj je šlo narobe :(")
            console.log('error')
          }
        })
      }
    },
    addMessage(message) {
      this.messages[message.index] = message.text;
    }
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
}
.logo {
  display: none;
  position: fixed;
  z-index: 1000;
  left: 40px;
  top: 30px;
}
.logo img {
  width: 157px;
  height: 152px;
}
@media (min-width: 992px) {
  .logo {
    display: block;
  }
}
</style>
