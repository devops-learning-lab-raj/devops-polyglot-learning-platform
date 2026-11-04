type Lesson = { title: string; level: string };
const lessons: Lesson[] = [
  { title: "Container builds", level: "Beginner" },
  { title: "Release promotion", level: "Advanced" }
];
console.log(JSON.stringify({ app: "learning-platform", lessons }, null, 2));
