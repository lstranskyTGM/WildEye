<template>
  <div class="h-100 container-fluid ms-0 ps-0 overflow-x-scroll" style="width: 100%">
    <div class="row w-100 h-100">
      <div class="col-xl-5 col-md-5 col-sm-12 col-12 h-100">
        <div class="w-100 h-100">
          <div class="card w-100 h-100 mh-100">
            <div class="card-header">
              <h5 class="card-subtitle">Beschreibung</h5>
            </div>
            <div class="card-body overflow-y-auto">
              <p>
                Das Diplomprojekt "WildEye" wird ausgetragen als finales Projekt für die Höhere Technische Bundeslehranstalt des Technologischen Gewerbemuseums (TGM). Die Arbeit wird von einem Projektteam bestehend aus vier Personen durchgeführt, sodass es in vier Hauptteile aufgeteilt werden kann:
              </p>
              <ul>
                <li>Hardware</li>
                <li>Frontend</li>
                <li>Content Management System</li>
                <li>Künstliche Intelligenz</li>
              </ul>
              <p>
                Das Ziel dieses Diplomprojektes ist das Erstellen eines modularen und öffentlich einsehbaren Wildkamerasystems. Einzelne Wildkameras können mittels einer Weboberfläche konfiguriert und ausgelesen werden. Außerdem soll ein KI-System inkludiert werden, welches Tiere in den aufgenommenen Bildern erkennen und klassifizieren kann.
              </p>
            </div>
            <div class="card-footer">
              <small class="small">Last update: 2024-10-24</small>
            </div>
          </div>
        </div>
      </div>
      <div class="col-7 col-md-7 col-sm-12 col-12 h-100">
        <div class="w-100 h-100">
          <div class="card w-100 h-100 mh-100 mw-100">
            <div class="card-header">
              <h5 class="card-subtitle">Informationen und Aktuelles</h5>
            </div>
            <div class="card-body overflow-y-auto">
              <div v-for="update in updates" :key="update.title" >
                <update-component :alt="update.alt" :image="update.image" :title="update.title"></update-component>
              </div>
            </div>
            <div class="card-footer">
              <small>last update: 2025-01-14</small>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import UpdateComponent from "@/components/UpdateComponent.vue";

export default {
  name: 'AboutView',
  components: {
    UpdateComponent
  },
  data() {
    return {
      updates: [
        { image: require('@/assets/ai1.jpg'), alt: "KI-Modell", title: "KI-Modell trainiert und ausführbar! - 11.02.2025" },
        { image: require('@/assets/hardware_prototyp_1.png'), alt: "Hardwareprototyp erstellt", title: "Erster Hardwareprototyp erstellt! - 14.01.2025" },
        { image: require('@/assets/Development_server.png'), alt: "Development Server erstellt", title: "Development Server erstellt zum testen der API, Designänderungen! - 12.01.2025" },
        { image: require('@/assets/wildeye neuronales netzwerk.png'), alt: "Neuronales Netzwerk von Wildeye", title: "Erstes neuronales Netzwerk für WildEye erstellt! - 13.12.2024" },
        { image: require('@/assets/softwareloesung_design.png'), alt: "Aktivitätsdiagramm für die Softwarelösung", title: "Aktivitätsdiagramm für die Softwarelösung erstellt! - 11.12.2024" },
        { image: require('@/assets/v2_projektwebsite.png'), alt: "V2 der Projektwebseite fertig", title: "V2 der Projektwebseite fertig! - 11.12.2024" },
        { image: require('@/assets/new_website.png'), alt: "Neue Website - Layout fertig", title: "Neue Website mit fertigem Layout! - 11.12.2024" },
        { image: require('@/assets/strapi_logo.png'), alt: "Strapi Prototyp", title: "Schnittstellen Prototyp mit Strapi erstellt - 08.12.2024" },
        { image: require('@/assets/logo_digital.png'), alt: "Logo Digitalisiert", title: "Logo wurde digitalisiert - 04.12.2024" },
        { image: require('@/assets/figma_mockup.png'), alt: "Mockup fertig, Usability Tests begonnen", title: "Mockup fertig, Usability Tests begonnen - 01.12.2024" },
        { image: require('@/assets/mockup_new_website.png'), alt: "Mockup neue Webseite", title: "Neues Mockup und Design! - 26.11.2024" },
        { image: require('@/assets/qrcode_wildeye_tech.png'), alt: "website qrcode", title: "Webseite jetzt gehostet! - 24.10.2024" },
        { image: require('@/assets/website_v1.png'), alt: "website", title: "V1 der Projektwebseite fertig - 24.10.2024" },
        { image: require('@/assets/WIldEye_Poster.jpg'), alt: "logo", title: "Poster fertig - 24.10.2024" },
        { image: require('@/assets/wildeye1.png'), alt: "logo", title: "Draft des Logos - 25.09.2024" },
        { image: require('@/assets/diplomprojekt_start.png'), alt: "logo", title: "Start Diplomprojekt mit Typst - 27.09.2024" }
      ]
    }
  }
}
</script>

<style>
.card {
  background-color: var(--wildeye-container-primary);
}
</style>