<template>
  <div class="signatures-popup">
    <div class="signatures-popup-content">
      <p>
        Zbranih <span>{{ counter }}</span> od 5000 podpisov
      </p>
      <div class="progress">
        <div class="progress-bar" role="progressbar" :aria-valuenow="counter" aria-valuemin="0" aria-valuemax="5000" :style="'width:' + progressBarWidth"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SignaturesPopup",
  async created() {
    await this.axios.get('https://api.djnd.si/getAllSignaturesAndCountForMultiple/?peticije=stanovanjskezadruge').then((res) => {
      if (res.status === 200) {
        this.counter = res.data.counter;
      }
    })
  },
  data() {
    return {
      counter: 0
    }
  },
  computed: {
    progressBarWidth() {
      return Math.round(this.counter/5000*100) + '%';
    }
  }
}
</script>

<style scoped>

.signatures-popup {
  display: none;
  position: fixed;
  z-index: 1000;
  background-image: url("../assets/signatures-blob.png");
  top: 50px;
  right: 50px;
  height: 162px;
  width: 440px;
}

@media (min-width: 992px) {
  .signatures-popup {
    display: block;
  }
}

.signatures-popup-content {
  margin: 40px;
}

p {
  font-family: 'Quicksand', sans-serif;
  font-size: 1.25rem;
  font-weight: 600;
  margin: 0.5rem 0;
}

.progress {
  margin: 0;
  width: 100%;
  height: 2rem;
  background-color: #efb046;
  border-radius: 2rem;
  padding: 2px;
  overflow: visible;
}

.progress-bar {
  background-color: #4d957f;
  border-radius: 2rem;
  height: 100%;
  position: relative;
  overflow: visible;
}

</style>
