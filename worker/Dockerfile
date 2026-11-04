FROM maven:3.9-eclipse-temurin-17 AS build
WORKDIR /src
COPY pom.xml .
COPY src ./src
RUN mvn -B package
FROM eclipse-temurin:17-jre
WORKDIR /app
COPY --from=build /src/target/java-worker-1.0.0.jar app.jar
CMD ["java", "-cp", "app.jar", "training.Worker"]