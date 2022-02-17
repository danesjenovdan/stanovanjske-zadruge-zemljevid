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
      type: String,
      default: ''
    },
  },
  data() {
    return {
      optionsNo: {
        'domovanje': [20, 21, 22, 25, 24, 48],
        'skupnost': [23, 10, 13, 47, 44, 15],
        'park': [30, 31, 32, 40, 45, 41],
        'pokrajina': [50, 51, 52, 53, 54, 60, 61, 62, 63, 64, 65],
      },
      objectNames: {
        10: 'Zadružna trgovina',
        13: 'Medgeneracijski center',
        15: 'Otroški vrtec',
        20: 'Dom za enega',
        21: 'Dom za dva',
        22: 'Dom za tri+',
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
