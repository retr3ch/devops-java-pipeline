FROM openjdk:11-jre-slim

WORKDIR /app

# Копируем JAR файл (используем wildcard)
COPY target/*.jar app.jar

EXPOSE 8080

CMD ["java", "-jar", "app.jar"]