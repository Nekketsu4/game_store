<template>
  <div id="Head">
    <header class="header">
      <div class="container">
        <div class="header__row">
          <div>
            <a class="logo" href="#"></a>
          </div>
          <div class="header__search">
            <input type="text" name="" id="" placeholder="Введите название игры">
          </div>
          <div class="header__login">
            <div class="header__sign">
              <button>Войти</button>
            </div>
            <div class="header__sign header__sign_active">
              <button>Регистрация</button>
            </div>
          </div>
        </div>
        <nav class="header__nav-row">
          <div class="header__nav-item"><a href="#">Каталог игр</a></div>
          <div class="header__nav-item"><a href="#">График выхода</a></div>
          <div class="header__nav-item"><a href="#">Как купить</a></div>
          <div class="header__nav-item"><a href="#">Активация игр</a></div>
          <div class="header__nav-item"><a href="#">Бонусы</a></div>
          <div class="header__nav-item"><a href="#">Контакты</a></div>
        </nav>
      </div>
    </header>
  </div>
</template>

<script>
  export default {
    name: "Head"
  }
</script>

<style scoped>

</style>