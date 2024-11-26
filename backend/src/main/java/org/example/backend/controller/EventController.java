package org.example.backend.controller;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/v1/events")
public class EventController {


    @PostMapping("/send")
    public ResponseEntity<String> sendSms() {
        return new ResponseEntity<>("SMS sent successfully.", HttpStatus.OK);
    }


}
