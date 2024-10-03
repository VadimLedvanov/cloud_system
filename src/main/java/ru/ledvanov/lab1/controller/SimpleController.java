package ru.ledvanov.lab1.controller;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@CrossOrigin(origins = "https://frontend.local")
public class SimpleController {

    @GetMapping("/api/hello")
    public String hello() {
        return "That's message from backend part!";
    }

    @GetMapping()
    public String info() {
        return "Это бэкенд часть, но вы не можете здесь ничего делать!";
    }
}
