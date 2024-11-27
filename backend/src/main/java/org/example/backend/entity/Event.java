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
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;
import lombok.Builder;
import org.springframework.data.geo.Point;

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
    private Long eventID;

    private String title;
    private Integer capacity;
    private String eventType;
    private String description;
    private String date;
    private String startTime;
    private String endTime;

    @ManyToOne
    @JoinColumn(name = "categoryID")
    private Category category;

    @ManyToMany
    @JoinTable(
            name = "eventcategories",
            joinColumns = @JoinColumn(name = "eventID"),
            inverseJoinColumns = @JoinColumn(name = "categoryID")
    )
    private List<Category> categories;

    @ManyToMany
    @JoinTable(
            name = "eventservices",
            joinColumns = @JoinColumn(name = "eventID"),
            inverseJoinColumns = @JoinColumn(name = "serviceID")
    )
    private List<Service> services;

    @ManyToMany
    @JoinTable(
            name = "organizers_events",
            joinColumns = @JoinColumn(name = "eventID"),
            inverseJoinColumns = @JoinColumn(name = "organizerID")
    )
    private List<Organizer> organizers;

    @OneToMany(mappedBy = "event", cascade = CascadeType.ALL)
    private List<Registration> registrations;

    @OneToMany(mappedBy = "event", cascade = CascadeType.ALL)
    private List<Review> reviews;

    @OneToMany(mappedBy = "event", cascade = CascadeType.ALL)
    private List<Announcement> announcements;

    @Column(columnDefinition = "geography(Point,4326)")
    private Point location;
}
