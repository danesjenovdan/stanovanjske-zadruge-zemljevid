<template>
  <div v-if="this.map" class="map-container" :class="{'frozen': tileChosen }">
    <div
      v-for="(item, index) in this.map"
      :key="index"
      class="tile"
      :id="'tile-' + index"
      :style="{'background-image': 'url(' + require('../assets/tiles/' + item + '.png') + ')'}"
      :class="{
        'taken-with-message': index in messages,
        'taken': !(index in messages) && item >= 10,
        'available': item < 10 && mapActive,
        'chosen': tileChosen === index,
        'show-message': messageTile === index
      }"
      @click="tileClicked(index);">
      <div v-if="index in messages" class="tile-message" :class="{
        'message-top': index >= 300,
        'message-bottom': index < 300
      }">
        <h4>Sporočilo</h4>
        <p>{{ messages[index] }}</p>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'Map',
  props: {
    map: {
      type: Array,
      default: ()=>[]
    },
    messages: {
      type: Object,
      default: ()=>{}
    },
    mapActive: {
      type: Boolean,
      default: false
    },
    tileChosen: {
      type: Number,
      default: null
    },
  },
  data() {
    return {
      messageTile: null,
    }
  },
  methods: {
    tileClicked(index) {
      this.messageTile = null;
      // tile not available
      if (this.map[index] >= 10) {
        if (index in this.messages) {
          this.showMessage(index);
        }
      } else { // tile still available
        // no tile has been chosen yet
        if (!this.tileChosen) {
          this.chooseTile(index);
        }
      }
    },
    showMessage(index) {
      this.messageTile = index;
    },
    chooseTile(index) {
      this.$emit('choose-tile', index);
    }
  }
}
</script>

<style scoped>
.map-container {
  width: 4800px;
}
.tile {
  float: left;
  position: relative;
  width: 48px;
  height: 48px;
  background-size: cover;
}
@media (min-width: 992px) {
  .map-container {
    width: 4800px;
  }
  .tile {
    float: left;
    position: relative;
    width: 48px;
    height: 48px;
    background-size: cover;
  }
}
.tile.chosen {
  outline: 2px solid black;
  z-index: 100;
}
.tile.taken-with-message:hover {
  cursor: pointer;
}
.tile.available:hover {
  cursor: pointer;
  outline: 2px solid black;
  z-index: 100;
}
.tile-message {
  display: none;
  position: absolute;
  z-index: 500;
  background-repeat: no-repeat;
  background-size: 100% 100%;
  min-width: 200px;
  left: -27px;
  padding: 20px;
}
.tile-message.message-top {
  background-image: url('../assets/tile-message-top.png');
  bottom: 100%;
  margin-bottom: 5px;
}
.tile-message.message-bottom {
  background-image: url('../assets/tile-message-bottom.png');
  top: 100%;
  margin-top: 5px;
}
.tile-message.message-bottom h4 {
  margin-top: 0.5rem;
}
.tile-message h4 {
  font-style: italic;
  font-family: 'Azeret Mono', monospace;
  margin-bottom: 0.5rem;
  margin-top: 0;
}
.tile-message p {
  margin-top: 0;
  margin-bottom: 0.5rem;
  font-family: 'Quicksand', sans-serif;
}
.show-message .tile-message {
  display: block;
}
</style>
