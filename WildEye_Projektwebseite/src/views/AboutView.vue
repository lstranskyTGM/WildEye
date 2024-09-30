<template>
  <div class=" h-100 container-fluid ms-0 ps-0 overflow-x-scroll" style="width: 100%">
    <div class="row w-100 h-100" >
      <div class="col-xl-8 col-md-7 col-sm-12 h-100 ">
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
              <small class="small">Last update: 2024-09-25</small>
            </div>
          </div>
        </div>
      </div>
      <div class="col-4 col-md-4 col-sm-12 h-100">
        <div class="w-100 h-100 ">
          <div class="card w-100 h-100 mh-100 mw-100">
            <div class="card-header">
              <h5 class="card-subtitle">Informationen und Aktuelles</h5>
            </div>
            <div class="card-body overflow-y-auto">
              <div class="card m-3 shadow">
                <div class="card-img-top img-fluid d-flex ">
                  <img src="@/assets/wildeye1.png" alt="logo" class="ms-auto me-auto mw-100 mh-100 rounded rounded-3">
                </div>
                <div class="card-header">
                  <div>
                    <p class="fs-5">Draft des Logos - 25.09.2025</p>
                  </div>
                </div>
              </div>
              <div class="card m-3 shadow">
                <div class="card-img-top img-fluid d-flex ">
                  <img src="@/assets/diplomprojekt_start.png" alt="logo" class="ms-auto me-auto mw-100 mh-100 rounded rounded-3">
                </div>
                <div class="card-header">
                  <div>
                    <p class="fs-5">Start Diplomprojekt mit Typst - 27.09.2025</p>
                  </div>
                </div>
              </div>
            </div>
            <div class="card-footer">
              <small>last update: 2024-09-25</small>
            </div>
          </div>

        </div>
      </div>
    </div>
  </div>
</template>
<script>

export default {
  name: 'AboutView',
  data() {
    return {
      name: 'AboutView',
      publicPath: process.env.BASE_URL
    }
  }
}
</script>