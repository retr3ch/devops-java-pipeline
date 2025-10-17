package main.java.com.devopsapp;

import static spark.Spark.*;

public class App {
    public static void main(String[] args) {
        port(8080);
        
        get("/", (req, res) -> {
            String version = "1.0.0";
            try {
                version = new java.util.Scanner(new java.io.File("version"))
                         .useDelimiter("\\Z").next();
            } catch (Exception e) {
                System.err.println("Version file not found, using default");
            }
            
            return "DevOps Java Application v" + version + " - Docker fix test!";
        });
        
        get("/health", (req, res) -> {
            res.type("application/json");
            return "{\"status\":\"healthy\",\"service\":\"devops-java-app\"}";
        });
        
        System.out.println("Server running on http://localhost:8080");
    }
}