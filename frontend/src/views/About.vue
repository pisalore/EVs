<template>
  <div class="text-center py-1">
    <h2 class="title">
      Take the best from the world <br />
      with EVs
    </h2>
    <h3 class="subtitle">
      With EVs is easier to discover the world and get the best from it. Enjoy
      us!
    </h3>
  </div>
  <div class="container p-1">
    <div class="col-12 wrapper">
      <h4>Story</h4>
      <div>
        <p class="pt-4">
          This project was thinked and developed by Lorenzo Pisaneschi, during a
          really hard summer exam sessions. EVs was born essentially for two
          main main reasons: the first is obviosly the academic one; the second,
          is the is the is the is the is the is the is the is the personal one:
          fact, I really desired of develop form A to Z, from design, to code
          and and deploy, my very first own own application. Evs is developed
          Django, a really Python framework, and Vue.js, a really powerful
          javascript framework. Although some parts could seem to simple or
          useless ( I hope not), I worked really hard for this project: from
          surveys with Google Forms, to User story mapping with Miro, to design
          using Figma, and then to to to code and deploy with Heroku. June 2021
        </p>
      </div>
    </div>
    <div class="col-12 wrapper">
      <h4>Idea</h4>
      <div>
        <p class="pt-4">
          The idea behind this project is simple: build an app which helps
          people to fine events in the respective cities and also aboard. we
          often find ourselves dealing with problems when we are dealing with
          events: are the events which we find effective? Is their organizer
          recommendable? Are the information about the event we are interested
          in trustable? And so on. <br />
          EVs is developed with this aim: make life easier to user which want
          enjoy events safely!
        </p>
      </div>
    </div>
    <div class="col-12 wrapper">
      <h4>Goal & Solution</h4>
      <div>
        <p class="pt-4">
          "Simple is better than complex." This is stated inside the "Zen of
          Python" (19-Aug-2004, (Tim Peters). For this reason, I clearly chosen
          Python for my backend, Django in particular. It isn incredible
          framework, which makes thins really simple. Alongside with Django I
          also used Django Rest Framework (I developed my APIs in 3 weeks) and
          S3, for data storing. <br />
          On the frontend part, Vue proved to be a really handy tool, easily
          easily integrated with Django. Finally for deployment: Heroku. A
          godsend!
        </p>
        <p>
          The project is hosted on GitHub:
          <a href="https://github.com/pisalore/evs">visit Evs repository</a>!
        </p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.title {
  font-style: normal;
  font-weight: 400;
  font-size: 48px;
  line-height: 56px;
  text-align: center;
  color: #1f6dad;
}

.subtitle {
  font-weight: 100;
  font-size: 36px;
  line-height: 42px;
  text-align: center;
  color: #575757;
}

.wrapper {
  margin-top: 40px;
  background: #ffffff;
  border-bottom: 1px solid #1f6dad;
  box-sizing: border-box;
}

h4 {
  font-style: normal;
  font-weight: 500;
  font-size: 36px;
  line-height: 42px;
  color: #2c98f0;
}

p {
  font-style: normal;
  font-weight: 300;
  font-size: 24px;
  line-height: 28px;
  color: #000000;
}
</style>
