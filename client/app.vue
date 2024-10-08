<template>
  <div class="page-container">
    <Header />
    <main class="main-content">
      <NuxtPage />
    </main>

    <Footer />
  </div>
</template>

<style lang="css" scoped>
.page-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.main-content {
  flex: 1;
}
</style>
