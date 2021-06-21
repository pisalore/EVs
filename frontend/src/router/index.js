import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";

import About from "../views/About";
import ContactUs from "../views/ContactUs";
import FAQ from "../views/FAQ";
import Events from "../views/Events";
import UserProfile from "../views/UserProfile";
import UserProfileEdit from "../views/UserProfileEdit";
import EventDetail from "../views/EventDetail";
import CreateEvent from "../views/CreateEvent";
import EditEvent from "../views/EventEdit";
import NotFound from "../views/NotFound";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/about",
    name: "About",
    component: About,
  },
  {
    path: "/faq",
    name: "FAQ",
    component: FAQ,
  },
  {
    path: "/contacts",
    name: "ContactUs",
    component: ContactUs,
  },
  {
    path: "/events",
    name: "Events",
    component: Events,
  },
  {
    path: "/profile",
    name: "Profile",
    component: UserProfile,
  },
  {
    path: "/edit-profile",
    name: "ProfileEdit",
    component: UserProfileEdit,
  },
  {
    path: "/events/:id",
    component: EventDetail,
    props: true,
  },
  {
    path: "/event-create",
    component: CreateEvent,
  },
  {
    path: "/event-edit/:id",
    component: EditEvent,
    props: true,
  },
  { path: "/:notFound(.*)", component: NotFound },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
