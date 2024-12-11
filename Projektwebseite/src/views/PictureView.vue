<template>
  <div class="w-100 h-100 d-flex align-items-center justify-content-center">
    <div class="row align-self-center h-100 w-100">
      <div class="row milestones h-100 w-100">
        <MilestoneComponent :entry = entry v-for="entry in milestones" :key="entry.title" class=""></MilestoneComponent>
      </div>
    </div>
  </div>
</template>

<script>
import TeamComponent from "@/components/TeamComponent.vue";
import MilestoneComponent from "@/components/MilestoneComponent.vue";

export default {
  name: 'PictureView',
  components: {
    MilestoneComponent
  },
  setup() {
  },
  data() {
    return {
      milestones: [
        {
          title:"Machbarkeit fertig",
          desc:"Die Machbarkeitsstudie für das Projekt ist abgeschlossen und die Wildkamera kann realisiert werden.",
          pic: "milestone1.svg",
          progress: "25%",
          date: "20.12.2024",
          color: "#"
        },
        {
          title:"Erste Bildaufnahme und Bilderkennung",
          desc:"Es wurde eine erste Bildaufnahme aufgenommen, welche mittels Bilderkennung analysiert und klassifiziert wurde.",
          pic: "milestone2.svg",
          progress: "25%",
          date: "19.01.2024"
        },
        {
          title:"Prototyp fertig",
          desc:"Es wurde der erste Prototyp der Wildkamera erstellt. Dieser kann aufnahmen tätigen, welche auf der Webseite einsehbar sind.",
          pic: "milestone3.svg",
          progress: "0%",
          date: "27.01.2025"
        },
        {
          title:"Testen fertig",
          desc:"Der Prototyp der Wildkamera wurde auf Funktionalität getestet und ist bereit für den Einsatz.",
          pic: "milestone4.svg",
          progress: "0%",
          date: "02.03.2025"
        }
      ]
    }
  },
  methods: {

  },
  computed: {
  },
  watch: {
  },
  mounted() {
  },
  beforeDestroy() {
  },
  destroyed() {
  }
}
</script>

<style scoped>
.milestones{
  width: 100%;
  max-height: 100%;
  overflow-y: auto;
  height: 100%;
}

@media (max-width: 962px) {
  .milestones {
    width: 88%;
  }
}
</style>