package org.example.backend.entity;

import jakarta.persistence.Column;
import jakarta.persistence.EmbeddedId;
import jakarta.persistence.Entity;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.MapsId;
import jakarta.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDate;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Entity
@Table(name = "reviews")
public class Review {

    @EmbeddedId
    private ReviewId id;

    @ManyToOne
    @MapsId("userId")
    @JoinColumn(name = "userid", nullable = false)
    private User user;

    @ManyToOne
    @MapsId("eventId")
    @JoinColumn(name = "eventid", nullable = false)
    private Event event;

    @Column(nullable = false)
    private Integer rating;

    @Column(columnDefinition = "text")
    private String comment;

    @Column(nullable = false)
    private LocalDate date;
}