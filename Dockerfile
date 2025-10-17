FROM openjdk:11-jre-slim

WORKDIR /app

# Копируем JAR файл (имя должно совпадать с pom.xml)
COPY target/pipeline-manager-1.0.0.jar app.jar

EXPOSE 8080

CMD ["java", "-jar", "app.jar"]