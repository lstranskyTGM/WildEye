<template>
  <div class="vh-100 vw-100 overflow-hidden edge_color">
    <div class="row-cols-2 d-flex w-100 h-100" style="padding-top: 2%">
      <div class="col-xxl-1 col-xl-1 col-lg-1 col-md-2 col-sm-12 edge_color">
        <div class="d-flex h-100 w-100">
          <div class="row-cols-1 ms-auto me-auto h-100">
            <nav class="mt-0 h-100 w-100 align-content-start d-flex flex-column">
              <div class="col d-flex justify-content-center align-content-center">
                <img src="@/assets/logo_v2_1.png" class="card-img-top img-fluid" style="object-fit: contain; width: 70%;">
              </div>
              <div class="overflow-y-auto h-100 flex-grow-1">
                <div class="col">
                  <router-link to="/" class="text-decoration-none text-reset text-center d-grid">
                    <div class="ratio ratio-1x1 bg-body rounded-3 w-75 ms-auto me-auto " style="height: 100%; width: 100%;">
                      <div class="d-flex justify-content-center align-items-center w-100 h-100 ">
                        <div class="shadow justify-content-center align-content-center rounded-3" style="width: 83%; height: 90%;">
                          <i class="bi bi-kanban w-100 d-block" style="font-size: 2rem; color: #a6b5cc;"></i>
                          <small class="w-100">Dashboard</small>
                        </div>
                      </div>
                    </div>
                  </router-link>
                </div>
                <div class="col mt-3">
                  <router-link to="/picture" class="text-decoration-none text-reset text-center">
                    <div class="ratio ratio-1x1 bg-body p-2 rounded-3 w-75 ms-auto me-auto " style="height: 100%; width: 100%;">
                      <div class="d-flex justify-content-center align-items-center w-100 h-100 ">
                        <div class="shadow justify-content-center align-content-center rounded-3" style="width: 83%; height: 90%;">
                          <i class="bi bi-images w-100 d-block" style="font-size: 2rem; color: #a6b5cc"></i>
                          <small class="w-100">Pictures</small>
                        </div>
                      </div>
                    </div>
                  </router-link>
                </div>
                <div class="col mt-3">
                  <router-link to="/about" class="text-decoration-none text-reset text-center">
                    <div class="ratio ratio-1x1 bg-body p-2 rounded-3 w-75 ms-auto me-auto " style="height: 100%; width: 100%;">
                      <div class="d-flex justify-content-center align-items-center w-100 h-100 ">
                        <div class="shadow justify-content-center align-content-center rounded-3" style="width: 83%; height: 90%;">
                          <i class="bi bi-broadcast w-100 d-block" style="font-size: 2rem; color: #a6b5cc"></i>
                          <small class="w-100">Live</small>
                        </div>
                      </div>
                    </div>
                  </router-link>
                </div>
                <div class="col mt-3">
                  <router-link to="/map" class="text-decoration-none text-reset text-center">
                    <div class="ratio ratio-1x1 bg-body p-2 rounded-3 w-75 ms-auto me-auto " style="height: 100%; width: 100%;">
                      <div class="d-flex justify-content-center align-items-center w-100 h-100 ">
                        <div class="shadow justify-content-center align-content-center rounded-3" style="width: 83%; height: 90%;">
                          <i class="bi bi-map w-100 d-block" style="font-size: 2rem; color: #a6b5cc"></i>
                          <small class="w-100 pt-0 mt-0">Map</small>
                        </div>
                      </div>
                    </div>
                  </router-link>
                </div>
                <div class="col mt-5">
                  <div class="ratio ratio-1x1 bg-body p-2 rounded-3 w-75 ms-auto me-auto " style="height: 100%; width: 100%;">
                    <div class="d-flex justify-content-center align-items-center w-100 h-100 ">
                      <div class="shadow justify-content-center align-content-center rounded-3" style="width: 83%; height: 90%;">
                        <i class="bi-0-circle-fill d-block" style="font-size: 2rem; color: #a6b5cc"></i>
                        <small class="w-100">Account</small>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

            </nav>

          </div>

        </div>
      </div>
      <div class="col-11 ms-auto me-0 edge_color pe-0 ps-0">
        <div class="w-100 h-100 rounded-top-5 rounded-end-0 bg-white me-0 ms-0 pe-0 ps-0">
          <div class="p-3 h-100 w-100">
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