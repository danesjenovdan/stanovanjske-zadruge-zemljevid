<template>
  <div>
    <div v-for="i in optionsNo[variations]" :key="i" class="object-option" @click="placeOnMap(i)">
      <div class="object-img">
        <img :src="require('../assets/tiles/' + i + '.png')" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ObjectVariations",
  props: {
    variations: {
      type: Number,
      default: 0
    },
  },
  data() {
    return {
      optionsNo: {
        1: [10, 11, 12, 13, 14, 15],
        2: [20, 21, 22, 23, 24, 25],
        3: [30, 31, 32, 33, 34, 35],
        4: [40, 41, 42, 43, 44, 45, 46, 47],
        5: [50, 51, 52, 53, 54],
        6: [60, 61, 62, 63, 64, 65]
      }
    }
  },
  methods: {
    placeOnMap(i) {
      this.$emit('place-on-map', i);
    }
  }
}
</script>

<style scoped>

</style>
