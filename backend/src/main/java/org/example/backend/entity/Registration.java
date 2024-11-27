package org.example.backend.entity;

import jakarta.persistence.Column;
import jakarta.persistence.EmbeddedId;
import jakarta.persistence.Entity;
import jakarta.persistence.EnumType;
import jakarta.persistence.Enumerated;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.MapsId;
import jakarta.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.example.backend.enums.RegistrationStatus;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Entity
@Table(name = "registrations")
public class Registration {

    @EmbeddedId
    private RegistrationId id; // Birleşik anahtar sınıfı

    @ManyToOne
    @MapsId("userId")
    @JoinColumn(name = "userid", nullable = false)
    private User user;

    @ManyToOne
    @MapsId("eventId")
    @JoinColumn(name = "eventid", nullable = false)
    private Event event;

    @Column(nullable = false, length = 100)
    private String ticket; // Ticket bilgisi, varchar(100)

    @Enumerated(EnumType.STRING)
    @Column(nullable = false)
    private RegistrationStatus status; // Enum türü (registrationstatusenum)

    @Column(nullable = false)
    private java.time.LocalDate date; // Tarih alanı
}