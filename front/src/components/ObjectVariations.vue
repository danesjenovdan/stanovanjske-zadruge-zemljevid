<template>
  <div class="object-panel">
    <div v-for="i in optionsNo[variations]" :key="i" class="object-option" @click="placeOnMap(i)">
      <div class="object-img">
        <img :src="require('../assets/tiles/' + i + '.png')" />
      </div>
      <span>{{ objectNames[i] }}</span>
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
        4: [40, 41, 42, 43, 44, 45, 46, 47, 48],
        5: [50, 51, 52, 53, 54],
      },
      objectNames: {
        10: 'Zadružna trgovina',
        15: 'Otroški vrtec',
        13: 'Medgeneracijski center',
        20: 'Dom za enega',
        21: 'Dom za dva',
        22: 'Dom za tri',
        23: 'Velika jedilnica',
        24: 'Skupna pralnica',
        25: 'Skupnostno stanovanje',
        30: 'Travnik',
        31: 'Hrast',
        32: 'Smreka',
        40: 'Športno igrišče',
        41: 'Sosedski bazen',
        44: 'Otroško igrišče',
        45: 'Miren kotiček',
        47: 'Vrtiček',
        48: 'Kolesarnica'
      }
    }
  },
  methods: {
    placeOnMap(i) {
      this.$emit('choose-variation', i);
    }
  }
}
</script>

<style scoped>
.object-panel {
  display: flex;
  flex-wrap: wrap;
}
</style>
