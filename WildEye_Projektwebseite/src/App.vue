<template>
  <div class="vh-100 vw-100 overflow-hidden edge_color">
    <div class="row-cols-2 d-flex w-100 h-100" style="padding-top: 2%">
      <div class="col-xxl-1 col-xl-1 col-lg-1 col-md-2 col-sm-12 edge_color">
        <div class="d-flex h-100 w-100">
          <div class="row-cols-1 ms-auto me-auto h-100">
            <nav class="mt-0 h-100 w-100 align-content-start d-flex flex-column">
              <div class="col d-flex justify-content-center align-content-center pb-3">
                <img src="@/assets/wildeye1.png" class="card-img-top img-fluid rounded rounded-3" style="object-fit: contain; width: 70%;">
              </div>
              <div class="overflow-y-auto h-100 flex-grow-1">
                <div class="col">
                  <router-link to="/" class="text-decoration-none text-reset text-center d-grid">
                    <div class="ratio ratio-1x1 bg-body rounded-3 w-75 ms-auto me-auto " style="height: 100%; width: 100%;">
                      <div class="d-flex justify-content-center align-items-center w-100 h-100 ">
                        <div class="shadow justify-content-center align-content-center rounded-3" style="width: 80%; height: 90%;">
                          <i class="bi bi-person-vcard" style="font-size: 2rem; color: #a6b5cc"></i>
                          <p class="small">Team</p>
                        </div>
                      </div>
                    </div>
                  </router-link>
                </div>
                <div class="col mt-3">
                  <router-link to="/about" class="text-decoration-none text-reset text-center">
                    <div class="ratio ratio-1x1 bg-body p-2 rounded-3 w-75 ms-auto me-auto " style="height: 100%; width: 100%;">
                      <div class="d-flex justify-content-center align-items-center w-100 h-100 ">
                        <div class="shadow justify-content-center align-content-center rounded-3" style="width: 80%; height: 90%;">
                          <i class="bi  bi-journal-richtext" style="font-size: 2rem; color: #a6b5cc"></i>
                          <p class="small">Projekt</p>
                        </div>
                      </div>
                    </div>
                  </router-link>
                </div>
                <div class="col mt-3">
                  <router-link to="/picture" class="text-decoration-none text-reset text-center">
                    <div class="ratio ratio-1x1 bg-body p-2 rounded-3 w-75 ms-auto me-auto " style="height: 100%; width: 100%;">
                      <div class="d-flex justify-content-center align-items-center w-100 h-100 ">
                        <div class="shadow justify-content-center align-content-center rounded-3" style="width: 80%; height: 90%;">
                          <i class="bi bi-card-checklist" style="font-size: 2rem; color: #a6b5cc"></i>
                          <p class="small">Meilensteine</p>
                        </div>
                      </div>
                    </div>
                  </router-link>
                </div>
<!--                <div class="col mt-3">
                  <router-link to="/map" class="text-decoration-none text-reset text-center">
                    <div class="ratio ratio-1x1 bg-body p-2 rounded-3 w-75 ms-auto me-auto " style="height: 100%; width: 100%;">
                      <div class="d-flex justify-content-center align-items-center w-100 h-100 ">
                        <div class="shadow justify-content-center align-content-center rounded-3" style="width: 80%; height: 80%;">
                          <i class="bi bi-map" style="font-size: 2rem; color: #a6b5cc"></i>
                          <p>Map</p>
                        </div>
                      </div>
                    </div>
                  </router-link>
                </div>
                <div class="col mt-5">
                  <div class="ratio ratio-1x1 bg-body p-2 rounded-3 w-75 ms-auto me-auto " style="height: 100%; width: 100%;">
                    <div class="d-flex justify-content-center align-items-center w-100 h-100 ">
                      <div class="shadow justify-content-center align-content-center rounded-3" style="width: 80%; height: 80%;">
                        <i class="bi-0-circle-fill" style="font-size: 2rem; color: #a6b5cc"></i>
                        <p>Account</p>
                      </div>
                    </div>
                  </div>
                </div>-->
              </div>

            </nav>

          </div>

        </div>
      </div>
      <div class="col-11 ms-auto me-0 edge_color pe-0 ps-0">
        <div class="w-100 h-100 rounded-top-5 rounded-end-0 bg-white me-0 ms-0 pe-0 ps-0">
          <div class="p-2 h-100 w-100 bg-gradient bg-light rounded-top-5 rounded-end-0">
            <router-view/>
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<style>
.edge_color{
  background-color: #e7e7e7;
}
</style>
<script>
</script>