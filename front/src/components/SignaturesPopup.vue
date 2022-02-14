<template>
  <div class="signatures-popup">
    <div class="signatures-popup-content">
      <p>
        Zbranih <span>{{ counter }}</span> od {{ signaturesGoal }} podpisov
      </p>
      <div class="progress">
        <div class="progress-bar" role="progressbar" :aria-valuenow="counter" aria-valuemin="0" :aria-valuemax="signaturesGoal" :style="'width:' + progressBarWidth"></div>
      </div>
      <p class="subtitle">1 podpis = 1 gradnik</p>
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
      counter: 0,
      signaturesGoal: 3000
    }
  },
  computed: {
    progressBarWidth() {
      let progressBarWidth = Math.ceil(this.counter/this.signaturesGoal*100)
      if (progressBarWidth < 5) {
        progressBarWidth = 5;
      }
      return progressBarWidth + '%';
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

.signatures-popup-content .subtitle {
  font-size: 1rem;
  margin-top: 0.25rem;
  margin-left: 0.25rem;
}

p {
  font-family: 'Quicksand', sans-serif;
  font-size: 1.25rem;
  font-weight: 600;
  margin: 0.75rem 0;
}

.progress {
  margin: 0;
  width: 100%;
  height: 1.5rem;
  background-color: #EFB046;
  border-radius: 2rem;
  padding: 4px;
  overflow: visible;
}

.progress-bar {
  background-color: #4d957f;
  border-radius: 1rem;
  height: 100%;
  position: relative;
  overflow: visible;
}

</style>
