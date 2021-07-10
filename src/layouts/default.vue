<template >
  <div class="dark:text-white">
    <Container border="b gray-200 dark:gray-600">
      <NavBar />
    </Container>
    <router-view />
    <Container border="t gray-200 dark:gray-600">
      <Footer />
    </Container>
  </div>
</template>
