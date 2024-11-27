package org.example.backend.entity;

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


@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Entity
@Table(name = "eventcategories")
public class EventCategory {

    @EmbeddedId
    private EventCategoryId id;

    @ManyToOne
    @MapsId("eventId")
    @JoinColumn(name = "eventid", nullable = false)
    private Event event;

    @ManyToOne
    @MapsId("categoryId")
    @JoinColumn(name = "categoryid", nullable = false)
    private Category category;
}