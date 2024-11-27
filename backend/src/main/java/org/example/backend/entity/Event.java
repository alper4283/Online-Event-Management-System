package org.example.backend.entity;

import jakarta.persistence.CascadeType;
import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.JoinTable;
import jakarta.persistence.ManyToMany;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.OneToMany;
import jakarta.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.geo.Point;

import java.time.LocalDate;
import java.time.LocalTime;
import java.util.List;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Entity
@Table(name = "events")
public class Event {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "eventid")
    private Long eventId;

    @Column(nullable = false, length = 255)
    private String title;

    @Column(nullable = false)
    private Integer capacity;

    @Column(name = "eventtype", nullable = false)
    private String eventType;

    @Column(columnDefinition = "text")
    private String description;

    @Column(nullable = false)
    private LocalDate date;

    @Column(name = "starttime", nullable = false)
    private LocalTime startTime;

    @Column(name = "endtime", nullable = false)
    private LocalTime endTime;

    @ManyToOne
    @JoinColumn(name = "addressid")
    private Address address;

    @ManyToOne
    @JoinColumn(name = "organizedby")
    private Organizer organizer;

    @ManyToMany
    @JoinTable(
            name = "eventcategories",
            joinColumns = @JoinColumn(name = "eventid"),
            inverseJoinColumns = @JoinColumn(name = "categoryid")
    )
    private List<Category> categories;

    @ManyToMany
    @JoinTable(
            name = "eventservices",
            joinColumns = @JoinColumn(name = "eventid"),
            inverseJoinColumns = @JoinColumn(name = "serviceid")
    )
    private List<Service> services;

    @OneToMany(mappedBy = "event", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<Registration> registrations;

    @OneToMany(mappedBy = "event", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<Review> reviews;

    @OneToMany(mappedBy = "event", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<Announcement> announcements;

    @Column(columnDefinition = "geography(Point,4326)")
    private Point location;

    @Column(nullable = false)
    private Double price;
}