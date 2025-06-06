<template>
  <div class=" h-100 mh-100 d-flex align-items-center justify-content-center w-100 pe-3 pe-xxl-0">
    <div class="row align-self-center team mh-100 h-100" >
      <div class="row mh-100 me-auto h-100">
        <TeamComponent :entry = entry v-for="entry in entries" :key="entry.name" class="mh-100"></TeamComponent>
      </div>

    </div>
  </div>
</template>

<script>
import TeamComponent from "@/components/TeamComponent.vue";

export default {
  name: 'HomeView',
  components: {TeamComponent},
  data() {
    return {
      name: 'HomeView',
      entries: [
        {
          name: "Markus Rafeiner",
          c: "5AHITM",
          topic: "Erstellung einer modernen und reaktiven Webseite, in welcher der Benutzer alle seine Wildkameras einsehen und verwalten, sowie generelle Einstellungen übernehmen kann.",
          pic: "new_1.jpg",
          email: "mrafeiner@student.tgm.ac.at"
        },
        {
          name: "Leonhard Stransky",
          c: "5AHIT",
          topic: "Erstellung eines Prototyp einer Wildkamera mit 3D gedruckten Komponenten, welcher Bilder und Aufnahmen über Mobilfunk überträgt und als modularer Bausatz für Hobbyisten dienen kann.",
          pic: "new_3.jpg",
          email: "lstransky@student.tgm.ac.at",
          extra: "Projektleiter"
        },
        {
          name: "Felix Aust",
          c: "5AHIT",
          topic: "Realisierung einer sicheren Schnittstelle zwischen Kamera und Webseite, inklusive eines Datenbanksystems zur persistenten Speicherung; Entwurf eines ansprechenden und wiedererkennbaren Logos.",
          pic: "new_2.jpg",
          email: "faust@student.tgm.ac.at"
        },
        {
          name: "Julian Neuwirth",
          c: "5AHIT",
          topic: "Erstellung eines modernes künstliches Intelligenzsystems, um eine detaillierte Klassifizierung jener Tiere, die in den Aufnahmen der Kamera zu sehen sind, zu gewährleisten. ",
          pic: "julian.jpg",
          email:"jneuwirth@student.tgm.ac.at"
        }
      ],
      publicPath: process.env.BASE_URL
    }
  }
}
</script>

<style>
.team{
  max-width: 97%;
  max-height: 100%;
  overflow-y: auto;
  height: 100%;
}



</style>